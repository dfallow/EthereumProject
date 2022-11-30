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
directory = tk.StringVar()
machine_hash = tk.StringVar()
machine_token_id = tk.IntVar()
prescription_token_id = tk.IntVar()


def deploy_data_contract():
    print(deployContracts.w3.eth.accounts)
    print(doctor_account.get())

    contract, address = deployContracts.compile_contract_with_accounts(
        contractDetailsMachineData.abi,
        contractDetailsMachineData.bytecode,
        patient_account.get(),
        doctor_account.get()
    )

    variables.machine_data_contract_var = contract

    print(contract)

    print(address)

    return


def upload_files_from_machine(machine, dir):

    file_from_directory = os.listdir(dir)
    file_hash_array = []

    dir_path = os.path.dirname(os.path.realpath(__file__))

    if os.path.exists(dir_path + '/files'):
        print("Directory Already Exists")
    else:
        os.mkdir(dir_path + '/files')
        print("Directory Created")

    # store each file in ipfs
    for file_to_add in file_from_directory:
        print("FILE", file_to_add)
        file_hash = ipfs.store_file(dir + file_to_add)

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
        file_hash_array.append(new_file_hash)


        # TODO place this at the end
        os.remove(file_path)


        print("Patient", patient_account.get())
        print("machine token", machine_token_id.get())
        print("prescription token", prescription_token_id.get())

        data_token_id = contractInteraction.mint_data_nft(
            variables.machine_data_contract_var,
            new_file_hash,
            machine_token_id.get(),
            prescription_token_id.get()
        )

        print("MINTED TOKEN", data_token_id)


    print("FILE ARRAY", file_hash_array)    

    ## TODO mint the returned hashes 

    
        
    return

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

root.mainloop()