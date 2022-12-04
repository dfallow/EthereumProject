import os
import json
import tkinter as tk
from tkinter import *
from library import ipfs, deployContracts, contractDetailsMachineData, variables, contractInteraction


#root window
root = tk.Tk()
root.geometry("1200x500")
#root.resizable(False, False)
root.title('Upload Machine Files')

# store user input
deploy_contract_patient = tk.StringVar()
deploy_contract_doctor = tk.StringVar()
machine_hash = tk.StringVar()
machine_token_id = tk.IntVar()
prescription_token_id = tk.IntVar()
directory_with_files = tk.StringVar()
transfer_contract_to_account = tk.StringVar()
transfer_nfts_to_account = tk.StringVar()
nft_token_list = tk.StringVar()
account_logged_in = tk.StringVar()
current_contract_address = tk.StringVar()
current_contract_owner = tk.StringVar()
tokens_from_uploaded_files = tk.StringVar()

### Functions ###

def initial_account_load():
    set_entry_value(logged_in_entry, deployContracts.w3.eth.default_account)
    
    
def deploy_data_contract():
    
    print("\nThe Account that will deploy the contract", deploy_contract_patient.get())
    deployContracts.change_default_account(deploy_contract_patient.get())
    contract, address, hash, receipt = deployContracts.compile_contract_with_accounts(
        contractDetailsMachineData.abi,
        contractDetailsMachineData.bytecode,
        deploy_contract_patient.get(), # patient deploys contract
        deploy_contract_doctor.get() # doctor is only registered
    )
    set_entry_value(logged_in_entry, deploy_contract_patient.get())

    variables.machine_data_contract_var = contract
    current_contract_address.set(address)
    #uploadMachineFiles.set_contract_address(address)
    set_entry_value(current_contract, address)
    set_entry_value(contract_owner_entry, deploy_contract_patient.get())

    print("\nThe Receipt which is given after the construction transact\n", receipt, "\n")
    print("The deployed machine contract", variables.machine_data_contract_var)
    print("The deployed contracts address", current_contract_address.get())

    return


def upload_files_from_machine():
    

    # gets files from user inputted directory
    file_from_directory = os.listdir(directory_with_files.get())

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
        file_hash = ipfs.store_file(directory_with_files.get() + file_to_add)
        original_hash_array.append(file_hash)

        json_info = {
            'fileHash': file_hash,
            'fileUrl': "https://ipfs.io/ipfs/" + file_hash,
            'machine_hash': machine_hash.get(),
            'machine_token': machine_token_id.get(),
            'precription_token': prescription_token_id.get()
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
        add_token_to_list(data_token_id)

    print("\nOriginal files, IPFS hash array:\n", original_hash_array)
    print("\nAltered files, IPFS hash array:\n", altered_hash_array)    
        
    return

def transfer_contract_ownership():
    
    contractInteraction.transfer_contract_ownership(
        variables.machine_data_contract_var,
        transfer_contract_to_account.get()
    )
    
    new_logged_user = deployContracts.change_default_account(transfer_contract_to_account.get())
    
    set_entry_value(contract_owner_entry, transfer_contract_to_account.get())
    set_entry_value(logged_in_entry, new_logged_user)
    
def transfer_ownership_mulitple_nfts():
    
    
    tokens = nft_token_list.get()
    
    print("TOKENS", tokens)
    
    # creates token array and converts string values to ints
    test = tokens.split(',')
    print("TEST", test)
    
    for i in range(0, len(test)):
        test[i] = int(test[i])
    
    #token_array = [eval(i) for i in test]
    
    #for each in token_array:
    #    print(type(each))
    
    contractInteraction.transfer_token_ownership(
        variables.machine_data_contract_var,
        transfer_nfts_to_account.get(),
        test
    )
    
    return
        

## Tkinter ##


# deploy contract & upload files frame
deploy_upload = Frame(root)
deploy_upload.pack(side=LEFT, fill='x', padx=10, pady=10, expand=True)

# frame label
deploy_upload_label = Label(deploy_upload, text="Deploy and Upload")
deploy_upload_label.pack(fill='x')

# patient account -> deploys the machine data contract
account_label = Label(deploy_upload, text="Enter Patient Account")
account_label.pack(fill='x', pady=10)

account_entry = Entry(deploy_upload, textvariable=deploy_contract_patient)
account_entry.pack(fill='x')

# doctor account -> is registed with the data contract
account_label = Label(deploy_upload, text="Enter Doctor Account")
account_label.pack(fill='x')

account_entry = Entry(deploy_upload, textvariable=deploy_contract_doctor)
account_entry.pack(fill='x')

# deploy contract button
deploy_btn = Button(
    deploy_upload,
    text="Deploy Contract",
    command=deploy_data_contract
)
deploy_btn.pack(fill='x', pady=10)

# registered machine -> IPFS reference hash retieved earlier
machine_label = Label(deploy_upload, text="Enter Hash of Machine")
machine_label.pack(fill='x', pady=20)

machine_input = Entry(deploy_upload, textvariable=machine_hash)
machine_input.pack(fill='x')

# machine token id -> From when the machine NFT was minted
machine_label = Label(deploy_upload, text="Enter Machine Token ID")
machine_label.pack(fill='x')

machine_input = Entry(deploy_upload, textvariable=machine_token_id)
machine_input.pack(fill='x')

# prescription token id -> From when the prescription NFT was minted
prescription_label = Label(deploy_upload, text="Enter Prescription Token ID")
prescription_label.pack(fill='x')

prescription_input = Entry(deploy_upload, textvariable=prescription_token_id)
prescription_input.pack(fill='x')

# user directory input -> Directory where files to upload at located
directory_label = Label(deploy_upload, text="Enter Path to Files Directory")
directory_label.pack(fill='x')

directory_input = Entry(deploy_upload, textvariable=directory_with_files)
directory_input.pack(fill='x', )

# upload files button
button = Button(
    deploy_upload,
    text='Upload Files',
    command=upload_files_from_machine
)
button.pack(fill='x', pady=10)

# transfer ownership frame
transfer_frame = Frame(root)
transfer_frame.pack(side=LEFT, padx=10, pady=10, fill='x', expand=True)

# transfer frame label
transfer_frame_label = Label(transfer_frame, text="Transfer Ownership")
transfer_frame_label.pack(fill='x')

# transfer contract to account label
transfer_to_account_label = Label(transfer_frame, text="Transfer Contract To Account:")
transfer_to_account_label.pack(fill='x', pady=10)

# transfer contract to account address
transfer_to_account_entry = Entry(transfer_frame, textvariable=transfer_contract_to_account)
transfer_to_account_entry.pack(fill='x')

# transfer contract button
button = Button(
    transfer_frame,
    text='Transfer Contract',
    command=transfer_contract_ownership
)
button.pack(fill='x', pady=10)

# transfer to account for file NFTs
nfts_transfer_account_label = Label(transfer_frame, text="Transfer Files To Account:")
nfts_transfer_account_label.pack(fill='x')

nft_transfer_account_entry = Entry(transfer_frame, textvariable=transfer_nfts_to_account)
nft_transfer_account_entry.pack(fill='x')

# nfts to transfer
nfts_to_transfer_label = Label(transfer_frame, text="List of NTF Tokens to Transfer:")
nfts_to_transfer_label.pack(fill='x')

nfts_to_transfer_entry = Entry(transfer_frame, textvariable=nft_token_list)
nfts_to_transfer_entry.pack(fill='x')

# transfer contract button
button = Button(
    transfer_frame,
    text='Transfer NFTs',
    command=transfer_ownership_mulitple_nfts
)
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

# nft tokens from upload
nft_tokens_label = Label(details_frame, text="Token Ids of NFT uploaded")
nft_tokens_label.pack(fill='x')

nft_tokens_entry = Entry(details_frame, textvariable=tokens_from_uploaded_files)
nft_tokens_entry.pack(fill='x')

def set_contract_address(address):
    current_contract.delete(0, END)
    current_contract.insert(0, address)
    
def set_entry_value(entry, value):
    entry.delete(0, END)
    entry.insert(0, value)
    
def add_token_to_list(token_id):
    nft_tokens_entry.insert(END,str(token_id) + ",")
    
    
# show accounts in terminal when launched
print("\nList of accounts:")
deployContracts.show_accounts()
initial_account_load()
print("List of accounts", deployContracts.w3.eth.default_account)


root.mainloop()