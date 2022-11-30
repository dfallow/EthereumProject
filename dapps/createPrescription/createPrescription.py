import tkinter as tk
from tkinter import *
from library import ipfs, deployContracts, mintNFTs, contractDetailsPrescription, variables

# root window
root =  tk.Tk()
root.geometry("450x450")
root.resizable(False, False)
root.title('Create Prescription')

# store user input
file_dir = tk.StringVar()
doctor_account = tk.StringVar()
patient_account = tk.StringVar()

def deploy_prescription_contract():
    print(patient_account.get())

    contract, address = deployContracts.compile_contract_with_accounts(
        contractDetailsPrescription.abi,
        contractDetailsPrescription.bytecode,
        doctor_account.get(),
        patient_account.get()
        )

    variables.prescription_data_contract_var = contract

    print(contract)

    print(address)

    return

def create_prescription():

    print("CONTRACT", variables.prescription_data_contract_var)

    prescription_hash = ipfs.store_file(file_dir.get())

    prescription_token_id = mintNFTs.mint_prescription_nft(variables.prescription_data_contract_var, prescription_hash)

    print("TOKEN", prescription_token_id)

    return prescription_hash

# show accounts in terminal when launched
deployContracts.show_accounts()

## Tkinter ##

# deploy contract frame
deploy = Frame(root)
deploy.pack(padx=10, pady=10, fill='x', expand=True)

# patient account -> deploys the machine data contract
account_label = Label(deploy, text="Enter Patient Account")
account_label.pack(fill='x', expand=True)

account_entry = Entry(deploy, textvariable=patient_account)
account_entry.pack(fill='x', expand=True)

# doctor account -> is registed with the data contract
account_label = Label(deploy, text="Enter Doctor Account")
account_label.pack(fill='x', expand=True)

account_entry = Entry(deploy, textvariable=doctor_account)
account_entry.pack(fill='x', expand=True)

# deploy contract button
deploy_btn = Button(
    deploy,
    text="Deploy Contract",
    command=deploy_prescription_contract
)
deploy_btn.pack(fill='x', expand=True, pady=10)

# register machine frame
prescription = Frame(root)
prescription.pack(padx=10, pady=10, fill='x', expand=True)

# file directory
directory_label = Label(prescription, text="Enter Path to Machine File")
directory_label.pack(fill='x', expand=True)

directory_entry = Entry(prescription, textvariable=file_dir)
directory_entry.pack(fill='x', expand=True)
directory_entry.focus()

button = Button(
    prescription, 
    text='Register Machine', 
    command=create_prescription)
button.pack(fill='x', expand=True, pady=10)

root.mainloop()