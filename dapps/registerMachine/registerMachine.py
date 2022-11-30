import tkinter as tk
from tkinter import *
from library import ipfs, deployContracts, mintNFTs, contractDetailsMachine, variables
#from library.variables import machine_contract_var

# root window
root =  tk.Tk()
root.geometry("450x450")
root.resizable(False, False)
root.title('Register Machine')

# store user input
# TODO add account here
file_dir = tk.StringVar()
user_account = tk.StringVar()
contract_address = tk.StringVar()

def deploy_contract():
    print(deployContracts.w3.eth.accounts)
    print(user_account.get())
    contract, address = deployContracts.compile_and_deploy_contract(
        contractDetailsMachine.abi, 
        contractDetailsMachine.bytecode,
        user_account.get()
        )

    #print("MACHINE", machine_contract_var)
    variables.machine_contract_var = contract
    print("MACHINE", variables.machine_contract_var)
    contract_address.set(address)
    print("CONTRACT", contract)
    print("GET CONTRACT", variables.machine_contract_var)
    print("ADDRESS", contract_address.get())

    set_contract_address(contract_address.get())
    
    return contract, address

## 1. uploads machine file to ipfs
## 2. mints the returned hash as url
def register_machine_v1():
    print("CONTRACT", variables.machine_contract_var)
    #machine_contract.get(), contract_address.get(), file_dir.get()
    machine_hash = ipfs.store_file(file_dir.get())

    print("EWNGWEIOGN", variables.machine_contract_var)
    mintNFTs.mint_nft(variables.machine_contract_var, machine_hash)

    set_machine_info(machine_hash)

    return machine_hash, contract


# show accounts in terminal when launched
deployContracts.show_accounts()

## Tkinter ##

# deploy contract frame
deploy = Frame(root)
deploy.pack(padx=10, pady=10, fill='x', expand=True)

# user account
account_label = Label(deploy, text="Enter User Account")
account_label.pack(fill='x', expand=True)

account_entry = Entry(deploy, textvariable=user_account)
account_entry.pack(fill='x', expand=True)

# deploy contract button
deploy_btn = Button(
    deploy,
    text="Deploy Contract",
    command=deploy_contract
)
deploy_btn.pack(fill='x', expand=True, pady=10)

# register machine frame
resgister_machine = Frame(root)
resgister_machine.pack(padx=10, pady=10, fill='x', expand=True)

# file directory
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

# current contract frame
contract = Frame(root, height=20)
contract.pack(padx=10, pady=10, fill='x')

# contract label
contract_label = Label(contract, text="Current Contract Address:")
contract_label.pack(fill='x', expand=True)

# contract address
current_contract = Entry(contract)
current_contract.pack(fill='x', expand=True)

# registered machine
machine_label = Label(contract, text="Registerd machine:")
machine_label.pack(fill='x', expand=True)

added_machine = Entry(contract)
added_machine.pack(fill='x', expand=True)


def set_contract_address(address):
    current_contract.insert(0, address)

def set_machine_info(hash):
    added_machine.insert(0, hash)
    
root.mainloop()
