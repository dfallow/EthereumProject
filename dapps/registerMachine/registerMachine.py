import tkinter as tk
from tkinter import *
from library import ipfs, deployContracts, contractDetailsMachine, variables, contractInteraction


# root window
root =  tk.Tk()
root.geometry("900x500")
root.title('Register Machine')

# store user input
contract_owner_account = tk.StringVar()
deploy_transfer_btn = tk.StringVar()
file_dir = tk.StringVar()
target_account = tk.StringVar()
transfer_token_id = tk.IntVar()
contract_address = tk.StringVar()
previous_owner = tk.StringVar()
current_owner = tk.StringVar()
registered_machine_token = tk.IntVar()

def deploy_transfer_contract():
    
    if deploy_transfer_btn.get() == "Deploy Contract":
        print("List of accounts", deployContracts.w3.eth.accounts)
        print("\nThe Account that will deploy the contract", contract_owner_account.get())
        contract, address, hash, receipt = deployContracts.compile_and_deploy_contract(
            contractDetailsMachine.abi, 
            contractDetailsMachine.bytecode,
            contract_owner_account.get()
            )

        variables.machine_contract_var = contract
        contract_address.set(address)
        set_contract_address(contract_address.get())
        set_entry_value(current_owner_entry, address)

        print("\nThe Receipt which is given after the construction transact\n", receipt, "\n")
        print("The deployed machine contract", variables.machine_contract_var)
        print("The deployed contracts address", contract_address.get())
        
        set_deploy_transfer_btn_name("Transfer Contract Ownership")
        reset_entry(account_entry)
        
        return contract, address
        
    else:
        
        print("TEST")

    

## 1. uploads machine file to ipfs
## 2. mints the returned hash as url
def register_machine_v1():

    machine_hash = ipfs.store_file(file_dir.get())

    token_id = contractInteraction.mint_machine_nft(variables.machine_contract_var, machine_hash)

    set_machine_info(machine_hash)
    set_entry_value(machine_token_entry, token_id)
    
    reset_entry(directory_entry)

    print("\nThe hash of the machine file stored in IPFS", machine_hash)
    print("Access the file through this url:", "https://ipfs.io/ipfs/" + machine_hash)

    return machine_hash

def transfer_token():
    
    return


# show accounts in terminal when launched
deployContracts.show_accounts()


## Tkinter ##


### User Interaction -> Left Side ###

# user interaction frame
user_frame = Frame(root, width=450)
user_frame.pack(side=LEFT, padx=10, pady=10, expand=True)

# target account -> delpoy contract or transfer ownership to
account_label = Label(user_frame, text="Enter Account That Will Own The Contract")
account_label.pack(fill='x', expand=True)

account_entry = Entry(user_frame, textvariable=contract_owner_account)
account_entry.pack(fill='x', expand=True)

# deploy contract button
deploy_btn = Button(
    user_frame,
    textvariable=deploy_transfer_btn,
    command=deploy_transfer_contract
)
deploy_btn.pack(fill='x', expand=True, pady=10)

# register machine frame
resgister_machine = Frame(user_frame)
resgister_machine.pack(pady=10, fill='x', expand=True)

# file directory -> path to the machine file
directory_label = Label(resgister_machine, text="Enter Path to Machine File")
directory_label.pack(fill='x', expand=True)

directory_entry = Entry(resgister_machine, textvariable=file_dir)
directory_entry.pack(fill='x', expand=True)
directory_entry.focus()

button = Button(
    resgister_machine, 
    text='Register Machine', 
    command=register_machine_v1)
button.pack(fill='x', expand=True, pady=10)

# tranfer token frame
transfer_token_frame = Frame(user_frame)
transfer_token_frame.pack(pady=10, fill='x', expand=True)

# target account
target_account_label = Label(transfer_token_frame, text="Enter Account To Transfer Machine To:")
target_account_label.pack(pady=10, fill='x', expand=True)

target_account_entry = Entry(transfer_token_frame, textvariable=target_account)
target_account_entry.pack(pady=10, fill='x', expand=True)

# token to transfer
token_transferring_label = Label(transfer_token_frame, text="Enter Token Id To Be Transferred")
token_transferring_label.pack(pady=10, fill='x', expand=True)

token_transferring_entry = Entry(transfer_token_frame, textvariable=transfer_token_id)
token_transferring_entry.pack(pady=10, fill='x', expand=True)

button = Button(
    transfer_token_frame, 
    text='Transfer Token', 
    command=transfer_token)
button.pack(fill='x', expand=True, pady=10)

### Contract Info -> Right Side ###

# contract details frame
details_frame = Frame(root, width=450)
details_frame.pack(side=RIGHT, fill='x', padx=10, pady=10, expand=True)

# contract label
contract_label = Label(details_frame, text="Current Contract Address:")
contract_label.pack(fill='x', expand=True)

# contract address
current_contract = Entry(details_frame)
current_contract.pack(fill='x', expand=True)

# previous owner
previous_owner_label = Label(details_frame,text="Previous Owner")
previous_owner_label.pack(fill='x', expand=True)

previous_owner_entry = Entry(details_frame, textvariable=previous_owner)
previous_owner_entry.pack(fill='x', expand=True)

# current owner
current_owner_label = Label(details_frame,text="Current Owner")
current_owner_label.pack(fill='x', expand=True)

current_owner_entry = Entry(details_frame, textvariable=current_owner)
current_owner_entry.pack(fill='x', expand=True)

# registered machine
machine_label = Label(details_frame, text="Registerd machine:")
machine_label.pack(fill='x', expand=True)

added_machine = Entry(details_frame)
added_machine.pack(fill='x', expand=True)

# registered machine token
machine_token_label = Label(details_frame, text="Token Of Newly Registered Machine")
machine_token_label.pack(fill='x', expand=True)

machine_token_entry = Entry(details_frame, textvariable=registered_machine_token)
machine_token_entry.pack(fill='x', expand=True)

def reset_entry(entry):
    entry.delete(0, END)

def set_deploy_transfer_btn_name(btn_text):
    deploy_transfer_btn.set(btn_text)

def set_contract_address(address):
    current_contract.delete(0, END)
    current_contract.insert(0, address)

def set_machine_info(hash):
    added_machine.delete(0, END)
    added_machine.insert(0, hash)
    
def set_entry_value(entry, value):
    entry.delete(0, END)
    entry.insert(0, value)
    
set_deploy_transfer_btn_name("Deploy Contract")
    
root.mainloop()
