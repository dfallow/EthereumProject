import tkinter as tk
from tkinter import *
from library import ipfs, deployContracts, contractDetailsPrescription, variables, contractInteraction

# root window
root =  tk.Tk()
root.geometry("1400x400")
root.resizable(False, False)
root.title('Create Prescription')

# store user input
file_dir = tk.StringVar()
doctor_account = tk.StringVar()
patient_account = tk.StringVar()
machine_token_id = tk.IntVar()
account_logged_in = tk.StringVar()
current_contract_address = tk.StringVar()
current_contract_owner = tk.StringVar()
token_id_from_minted_prescription = tk.IntVar()

def initial_account_load():
    set_entry_value(logged_in_entry, deployContracts.w3.eth.default_account)

def deploy_prescription_contract():
    print(patient_account.get())

    contract, address, hash, receipt = deployContracts.compile_contract_with_accounts(
        contractDetailsPrescription.abi,
        contractDetailsPrescription.bytecode,
        doctor_account.get(),
        patient_account.get()
    )

    set_entry_value(logged_in_entry, doctor_account.get())
    variables.prescription_data_contract_var = contract
    set_entry_value(current_contract, address)
    set_entry_value(contract_owner_entry, doctor_account.get())

    print(contract)

    print(address)

    return

def create_prescription():

    print("CONTRACT", variables.prescription_data_contract_var)

    prescription_hash = ipfs.store_file(file_dir.get())

    prescription_token_id = contractInteraction.mint_prescription_nft(variables.prescription_data_contract_var, prescription_hash, machine_token_id.get())

    print("TOKEN", prescription_token_id)
    show_token_id(prescription_token_id)

    return prescription_hash

def transfer_machine_token():
    
    contractInteraction.transfer_token_ownership(
        variables.machine_contract_var,
        patient_account.get(),
        machine_token_id.get()
    )
    
    return

# show accounts in terminal when launched
deployContracts.show_accounts()

## Tkinter ##

# deploy contract frame
deploy = Frame(root)
deploy.pack(side=LEFT, padx=10, pady=10, fill='x', expand=True)

# patient account -> deploys the machine data contract
account_label = Label(deploy, text="Enter Patient Account")
account_label.pack(fill='x')

account_entry = Entry(deploy, textvariable=patient_account)
account_entry.pack(fill='x')

# doctor account -> is registered with the data contract
account_label = Label(deploy, text="Enter Doctor Account")
account_label.pack(fill='x')

account_entry = Entry(deploy, textvariable=doctor_account)
account_entry.pack(fill='x')

# deploy contract button
deploy_btn = Button(
    deploy,
    text="Deploy Contract",
    command=deploy_prescription_contract
)
deploy_btn.pack(fill='x', pady=10)

# create prescription frame
prescription = Frame(root)
prescription.pack(side=LEFT,padx=10, pady=10, fill='x', expand=True)

# file directory
directory_label = Label(prescription, text="Enter Path to Prescription File")
directory_label.pack(fill='x')

directory_entry = Entry(prescription, textvariable=file_dir)
directory_entry.pack(fill='x')
directory_entry.focus()

# machine token id
token_label = Label(prescription, text = "Machine Token ID")
token_label.pack(fill='x')

token_entry = Entry(prescription, textvariable=machine_token_id)
token_entry.pack(fill='x')

button = Button(
    prescription, 
    text='Create Prescription', 
    command=create_prescription)
button.pack(fill='x', pady=10)

# transfer machine token ownership frame
transfer_frame = Frame(root)
transfer_frame.pack(side=LEFT, padx=10, pady=10, fill='x', expand=True)

# transfer frame label
transfer_frame_label = Label(transfer_frame, text="Transfer Machine Ownership To Patient")
transfer_frame_label.pack(fill='x')

# transfer token to account label
transfer_to_account_label = Label(transfer_frame, text="Transfer Machine To Patient:")
transfer_to_account_label.pack(fill='x', pady=10)

# transfer token to account address
transfer_to_account_entry = Entry(transfer_frame, textvariable=patient_account)
transfer_to_account_entry.pack(fill='x')

# transfer token button
button = Button(
    transfer_frame,
    text='Transfer Machine Token',
    command=transfer_machine_token)
button.pack(fill='x', pady=10)

# details frame
details_frame = Frame(root)
details_frame.pack(side=RIGHT, padx=10, pady=10, fill='x', expand=True)

# account logged in
logged_in_label = Label(details_frame, text="Account Logged In:")
logged_in_label.pack(fill='x')

logged_in_entry = Entry(details_frame)
logged_in_entry.pack(fill='x', pady=20)

# details label
details_label = Label(details_frame, text="Contract & NFT Details")
details_label.pack(fill='x', pady=20)

# contract label
contract_label = Label(details_frame, text="Current Contract Address:")
contract_label.pack(fill='x')

# contract address
current_contract = Entry(details_frame)
current_contract.pack(fill='x')

# contract owner
contract_owner_label = Label(details_frame, text="Current Contract Owner:")
contract_owner_label.pack(fill='x')

contract_owner_entry = Entry(details_frame)
contract_owner_entry.pack(fill='x')

# nft token
nft_token_label = Label(details_frame, text="Token Id of Minted Prescription")
nft_token_label.pack(fill='x')

nft_token_entry = Entry(details_frame, textvariable=token_id_from_minted_prescription)
nft_token_entry.pack(fill='x')

def set_contract_address(address):
    current_contract.delete(0, END)
    current_contract.insert(0, address)
    
def set_entry_value(entry, value):
    entry.delete(0, END)
    entry.insert(0, value)
    
def show_token_id(token_id):
    nft_token_entry.delete(0, END)
    nft_token_entry.insert(0, token_id)
    
# show accounts in terminal when launched
print("\nList of accounts:")
deployContracts.show_accounts()
initial_account_load()

root.mainloop()