import tkinter as tk
from tkinter import *
from library import deployContracts, contractDetailsPatientToken, variables, contractInteraction

# root window
root =  tk.Tk()
root.geometry("450x450")
root.resizable(False, False)
root.title('Add & View Patients')

# store user input
doctor_account = tk.StringVar()
patient_address = tk.StringVar()
patient_data_contract = tk.StringVar()
patient_prescription_contract = tk.StringVar()

def deploy_contract():

    contract, address = deployContracts.compile_and_deploy_contract(
        contractDetailsPatientToken.abi,
        contractDetailsPatientToken.bytecode,
        doctor_account.get()
    )

    variables.add_new_patient_contract_var = contract

    print(contract)

    print(address)

    return contract, address


def add_new_patient():

    patient_exists = contractInteraction.add_new_patient(
        variables.add_new_patient_contract_var,
        patient_address.get(),
        patient_data_contract.get(),
        patient_prescription_contract.get()
    )

    print("PATIENT EXISTS", patient_exists)

    #paddress, pcontract = variables.add_new_patient_contract_var.functions.getPatient(patient_address.get())

    

    

    return

# show accounts in terminal when launched
deployContracts.show_accounts()


## Tkinter ##

# deploy contract frame
deploy = Frame(root)
deploy.pack(padx=10, pady=10, fill='x', expand=True)

# user account
account_label = Label(deploy, text="Enter Doctor Account")
account_label.pack(fill='x', expand=True)

account_entry = Entry(deploy, textvariable=doctor_account)
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


root.mainloop()