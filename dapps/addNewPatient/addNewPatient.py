import tkinter as tk
from tkinter import *
from library import deployContracts, contractDetailsPatientToken, variables, contractInteraction, contractDetailsPrescription, contractDetailsMachineData

# root window
root =  tk.Tk()
root.geometry("450x450")
root.resizable(False, False)
root.title('Add & View Patients')

# store user input
doctor_address = tk.StringVar()
contract_address = tk.StringVar()
patient_address = tk.StringVar()
patient_data_contract = tk.StringVar()
patient_prescription_contract = tk.StringVar()

def deploy_contract():
    contract, address, hash, receipt = deployContracts.compile_and_deploy_contract(
        contractDetailsPatientToken.abi,
        contractDetailsPatientToken.bytecode,
        doctor_address.get() # doctor deploys contract
    )

    variables.add_new_patient_contract_var = contract
    contract_address.set(address)
    set_contract_address(address)

    print("\nThe Receipt which is given after the construction transact\n", receipt, "\n")
    print("The deployed machine contract", variables.add_new_patient_contract_var)
    print("The deployed contracts address", contract_address.get())

    return contract, address


def add_new_patient():

    patient_exists, patient, data_contract_address, prescription_contract_address = contractInteraction.check_for_patient_data(
        variables.add_new_patient_contract_var,
        patient_address.get()
    )
    
    print("PATIENT EXISTS:", patient_exists)

    if patient_exists:
        print("\nCannot add duplicate patient")
        print("\nPatient exists with data:")
        print("Account:", patient)
        print("Data contract address:", data_contract_address)
        print("Prescription contract address:", prescription_contract_address)
    else:
        #deploy data contract
        data_contract, data_contract_address, transaction_hash, transaction_receipt = deployContracts.compile_contract_with_accounts(
            contractDetailsMachineData.abi,
            contractDetailsMachineData.bytecode,
            patient_address.get(),
            doctor_address.get()
        )

        #deploy prescription contract
        prescription_contract, prescription_contract_address, transaction_hash, transaction_receipt = deployContracts.compile_contract_with_accounts(
            contractDetailsPrescription.abi,
            contractDetailsPrescription.bytecode,
            doctor_address.get(),
            patient_address.get()
        )

        patient, data, prescription = contractInteraction.add_new_patient(
            variables.add_new_patient_contract_var,
            patient_address.get(),
            data_contract_address,
            prescription_contract_address
        )

        print("\nPatient added with data:")
        print("Account:", patient)
        print("Data contract address:", data_contract_address)
        print("Prescription contract address:", prescription_contract_address)

    return

# show accounts in terminal when launched
print("\nList of accounts:")
deployContracts.show_accounts()


## Tkinter ##

# deploy contract frame
deploy = Frame(root)
deploy.pack(padx=10, pady=10, fill='x', expand=True)

# user account
account_label = Label(deploy, text="Enter Doctor Account")
account_label.pack(fill='x', expand=True)

account_entry = Entry(deploy, textvariable=doctor_address)
account_entry.pack(fill='x', expand=True)

# deploy contract button
deploy_btn = Button(
    deploy,
    text="Deploy Contract",
    command=deploy_contract
)
deploy_btn.pack(fill='x', expand=True, pady=10)

# add patient frame
patient = Frame(root)
patient.pack(padx=10, pady=10, fill='x', expand=True)

# patient account
account_label = Label(patient, text="Enter patient Account")
account_label.pack(fill='x', expand=True)

account_entry = Entry(patient, textvariable=patient_address)
account_entry.pack(fill='x', expand=True)

# data contract of patient address
account_label = Label(patient, text="Enter Data Contract Address")
account_label.pack(fill='x', expand=True)

account_entry = Entry(patient, textvariable=patient_data_contract)
account_entry.pack(fill='x', expand=True)

# prescription contract of patient address
account_label = Label(patient, text="Enter Prescription Contract Address")
account_label.pack(fill='x', expand=True)

account_entry = Entry(patient, textvariable=patient_prescription_contract)
account_entry.pack(fill='x', expand=True)

# add patient button
button = Button(
    patient, 
    text='Add New Patient', 
    command=add_new_patient)
button.pack(fill='x', expand=True, pady=10)

# details frame
details_frame = Frame(root)
details_frame.pack(padx=10, pady=10, fill='x', expand=True)

# contract label
contract_label = Label(details_frame, text="Current Contract Address:")
contract_label.pack(fill='x', expand=True)

# contract address
current_contract = Entry(details_frame)
current_contract.pack(fill='x', expand=True)

def set_contract_address(address):
    current_contract.delete(0, END)
    current_contract.insert(0, address)


root.mainloop()