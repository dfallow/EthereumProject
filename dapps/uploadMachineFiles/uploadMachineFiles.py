import os
import json
import tkinter as tk
from tkinter import *
from library import ipfs, deployContracts, contractDetailsMachineData, variables, contractInteraction


#root window
root = tk.Tk()
root.geometry("450x450")
#root.resizable(False, False)
root.title('Upload Machine Files')

# store user input
doctor_account = tk.StringVar()
patient_account = tk.StringVar()
contract_address = tk.StringVar()
directory = tk.StringVar()
machine_hash = tk.StringVar()
machine_token_id = tk.IntVar()
prescription_token_id = tk.IntVar()


def deploy_data_contract():
    print("List of accounts", deployContracts.w3.eth.accounts)
    print("\nThe Account that will deploy the contract", patient_account.get())

    contract, address, hash, receipt = deployContracts.compile_contract_with_accounts(
        contractDetailsMachineData.abi,
        contractDetailsMachineData.bytecode,
        patient_account.get(), # patient deploys contract
        doctor_account.get() # doctor is only registered
    )

    variables.machine_data_contract_var = contract
    contract_address.set(address)
    set_contract_address(address)

    print("\nThe Receipt which is given after the construction transact\n", receipt, "\n")
    print("The deployed machine contract", variables.machine_contract_var)
    print("The deployed contracts address", contract_address.get())

    return


def upload_files_from_machine(machine, dir):

    # gets files from user inputted directory
    file_from_directory = os.listdir(dir)

    # gets the current directory -> location where temporary files are stored
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("\nPath to current directory containing current file (uploadMachineFiles.py)")

    # the original files stored in IPFS
    original_hash_array = []
    # the altered files stored in IPFS
    altered_hash_array = []

    # checks if directory exists
    if os.path.exists(dir_path + '/files'):
        print("Directory Already Exists")
    else:
        os.mkdir(dir_path + '/files')
        print("Directory Did Not Exist\nCreated Directory")

    # store each file in ipfs
    for file_to_add in file_from_directory:

        print("Current file being added", file_to_add)
        file_hash = ipfs.store_file(dir + file_to_add)
        original_hash_array.append(file_hash)

        json_info = {
            'fileHash': file_hash,
            'fileUrl': "https://ipfs.io/ipfs/" + file_hash,
            'machine_hash': machine.get()
        }

        # creatting temporary .json file
        json_file = json.dumps(json_info)
        file_path = dir_path + "/files/dataFile" + str(file_from_directory.index(file_to_add)) + ".json"
        new_file = open(file_path, "x")
        new_file.write(json_file)
        new_file.close()

        # storing the newly created .json file in ipfs
        new_file_hash = ipfs.store_file(file_path)
        altered_hash_array.append(new_file_hash)

        # removes the temporary file
        os.remove(file_path)

        data_token_id = contractInteraction.mint_data_nft(
            variables.machine_data_contract_var,
            new_file_hash,
            machine_token_id.get(),
            prescription_token_id.get()
        )

        print("\nMINTED TOKEN", data_token_id)

    print("\nOriginal files, IPFS hash array:\n", original_hash_array)
    print("\nAltered files, IPFS hash array:\n", altered_hash_array)    
        
    return
        

# show accounts in terminal when launched
print("\nList of accounts:")
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
    command=deploy_data_contract
)
deploy_btn.pack(fill='x', expand=True, pady=10)

# frame
file_frame = Frame(root)
file_frame.pack(padx=10, pady=10, fill='x', expand=True)

# registered machine -> IPFS reference hash retieved earlier
machine_label = Label(file_frame, text="Enter Hash of Machine")
machine_label.pack(fill='x', expand=True)

machine_input = Entry(file_frame, textvariable=machine_hash)
machine_input.pack(fill='x', expand=True)

# machine token id -> From when the machine NFT was minted
machine_label = Label(file_frame, text="Enter Machine Token ID")
machine_label.pack(fill='x', expand=True)

machine_input = Entry(file_frame, textvariable=machine_token_id)
machine_input.pack(fill='x', expand=True)

# prescription token id -> From when the prescription NFT was minted
machine_label = Label(file_frame, text="Enter Prescription Token ID")
machine_label.pack(fill='x', expand=True)

machine_input = Entry(file_frame, textvariable=prescription_token_id)
machine_input.pack(fill='x', expand=True)

# user directory input -> Directory where files to upload at located
directory_label = Label(file_frame, text="Enter Path to Files Directory")
directory_label.pack(fill='x', expand=True)

directory_input = Entry(file_frame, textvariable=directory)
directory_input.pack(fill='x', expand=True)

# upload files button
button = Button(
    file_frame,
    text='Upload Files',
    command=lambda: upload_files_from_machine(machine_hash, directory.get())
)
button.pack(fill='x', expand=True)

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