import tkinter as tk
from tkinter import *
from library import deployContracts, contractDetailsPatientToken, variables, contractInteraction

# root window
root =  tk.Tk()
root.geometry("1350x450")
root.resizable(False, False)
root.title('Add & View Patients')

# store user input
logged_in_account = tk.StringVar()
doctor_account = tk.StringVar()
deploy_transfer_btn = tk.StringVar()
current_contract_address = tk.StringVar()
current_contract_owner = tk.StringVar()
patient_address = tk.StringVar()
patient_data_contract = tk.StringVar()
patient_prescription_contract = tk.StringVar()
patient_to_check = tk.StringVar()

def initial_account_load():
    set_entry_value(logged_in_entry, deployContracts.w3.eth.default_account)
    
def deploy_transfer_contract():
    
    if deploy_transfer_btn.get() == "Deploy Contract":
    
        deployContracts.change_default_account(doctor_account.get())

        contract, address, hash, receipt = deployContracts.compile_and_deploy_contract(
            contractDetailsPatientToken.abi,
            contractDetailsPatientToken.bytecode,
            doctor_account.get() # doctor deploys contract
        )

        variables.add_new_patient_contract_var = contract
        current_contract_address.set(address)
        set_contract_address(address)

        print("\nThe Receipt which is given after the construction transact\n", receipt, "\n")
        print("The deployed machine contract", variables.add_new_patient_contract_var)
        print("The deployed contracts address", current_contract_address.get())
        
        set_deploy_transfer_btn_name("Transfer Contract Ownership")
    
        set_entry_value(current_owner_entry, doctor_account.get())

        return contract, address
    
    else:
        
        contractInteraction.transfer_contract_ownership(
            variables.add_new_patient_contract_var,
            doctor_account.get()
        )
        
        new_logged_in_account = deployContracts.change_default_account(doctor_account.get())
        
        set_entry_value(logged_in_entry, new_logged_in_account)
        
        current_contract_owner.set(new_logged_in_account)
        set_entry_value(current_owner_entry, current_contract_owner.get())

def add_new_patient():

    patient_exists, patient, data, prescription = contractInteraction.add_new_patient(
        variables.add_new_patient_contract_var,
        patient_address.get(),
        patient_data_contract.get(),
        patient_prescription_contract.get()
    )

    print("PATIENT EXISTS", patient_exists)

    if patient_exists:
        print("\nCannot add duplicate patient")
    else:
        print("\nPatient added with data:")
        print("Account:", patient)
        print("Data contract address:", data)
        print("Prescription contract address:", prescription)

    return

def get_patient_status():
    
    exists, data_con, prescipt_con = contractInteraction.get_patient(
        variables.add_new_patient_contract_var,
        patient_to_check.get()
    )
    
    print("PATIENT EXISTS", exists)
    print("CONTRACT 1", data_con)
    print("CONTRACT 2", prescipt_con)
    
    if exists:
        set_entry_value(patient_status_entry, "Patient Assigned To Doctor")
    else:
        set_entry_value(patient_status_entry, "No Record Of Patient With Doctor")
    
    return

# show accounts in terminal when launched
print("\nList of accounts:")
deployContracts.show_accounts()


## Tkinter ##


### User Interaction -> Left Side ###

# user interaction frame
user_frame = Frame(root, width=450)
user_frame.pack(side=LEFT, fill='x', padx=10, pady=10, expand=True)

# target account -> delpoy contract
account_label = Label(user_frame, text="Doctor Account That Will Own The Contract:")
account_label.pack(fill='x', expand=True)

account_entry = Entry(user_frame, textvariable=doctor_account)
account_entry.pack(fill='x', expand=True)

# deploy contract button
deploy_btn = Button(
    user_frame,
    textvariable=deploy_transfer_btn,
    command=deploy_transfer_contract
)
deploy_btn.pack(fill='x', expand=True, pady=10)

# add patient frame
add_patient_frame = Frame(user_frame)
add_patient_frame.pack(pady=10, fill='x', expand=True)

# patient account
target_account_label = Label(add_patient_frame, text="Enter Patient Account To Add")
target_account_label.pack(pady=10, fill='x', expand=True)

target_account_entry = Entry(add_patient_frame, textvariable=patient_address)
target_account_entry.pack(fill='x', expand=True)

# patients data contract address
token_transferring_label = Label(add_patient_frame, text="Enter Patient Data Contract")
token_transferring_label.pack(fill='x', expand=True)

token_transferring_entry = Entry(add_patient_frame, textvariable=patient_data_contract)
token_transferring_entry.pack(fill='x', expand=True)

# patients prescription contract address
token_transferring_label = Label(add_patient_frame, text="Enter Patient Prescription Contract")
token_transferring_label.pack(fill='x', expand=True)

token_transferring_entry = Entry(add_patient_frame, textvariable=patient_prescription_contract)
token_transferring_entry.pack(fill='x', expand=True)

button = Button(
    add_patient_frame, 
    text='Assign Patient To Doctor',
    command=add_new_patient
    )
button.pack(fill='x', expand=True, pady=10)

### Logged In User Account ###

# logged in user frame
logged_in_frame = Frame(root, width=400)
logged_in_frame.pack(side=LEFT, fill='x', padx=10, pady=10, expand=True)

#logged in
logged_in_label = Label(logged_in_frame, text="Account Logged In:")
logged_in_label.pack(side=TOP, expand=True)

logged_in_entry = Entry(logged_in_frame, textvariable=logged_in_account.get())
logged_in_entry.pack(side=TOP, fill='x', pady=10, expand=True)


# contract label
contract_label = Label(logged_in_frame, text="Current Contract Address:")
contract_label.pack(fill='x', expand=True)

# contract address
current_contract = Entry(logged_in_frame)
current_contract.pack(fill='x', expand=True)

# current contract owner
current_owner_label = Label(logged_in_frame,text="Current Owner")
current_owner_label.pack(fill='x', expand=True)

current_owner_entry = Entry(logged_in_frame, textvariable=current_contract_owner)
current_owner_entry.pack(fill='x', expand=True)

# check patient frame
check_patient_frame = Frame(root)
check_patient_frame.pack(side=LEFT, padx=10, pady=10, fill='x', expand=TRUE)

# check patient -> patient account
check_patient_label = Label(check_patient_frame, text="Patient Account:")
check_patient_label.pack(fill='x', expand=True)

check_patient_entry = Entry(check_patient_frame, textvariable=patient_to_check)
check_patient_entry.pack(fill='x', expand=True)

button = Button(
    check_patient_frame, 
    text='Check Patient Belongs to Doctor',
    command=get_patient_status
    )
button.pack(fill='x', expand=True, pady=10)

# check patient -> patient exists
patient_status_label = Label(check_patient_frame, text="Patient Status:")
patient_status_label.pack(fill='x', expand=True)

patient_status_entry = Entry(check_patient_frame)
patient_status_entry.pack(fill='x', expand=True)

def set_contract_address(address):
    current_contract.delete(0, END)
    current_contract.insert(0, address)
    
def set_deploy_transfer_btn_name(btn_text):
    deploy_transfer_btn.set(btn_text)
    
def set_entry_value(entry, value):
    entry.delete(0, END)
    entry.insert(0, value)

set_deploy_transfer_btn_name("Deploy Contract")
initial_account_load()

root.mainloop()