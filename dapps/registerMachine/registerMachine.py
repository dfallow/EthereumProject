import easygui
import tkinter as tk
from tkinter import *
from library import ipfs, deployContracts, newContractDetails, mintNFTs

# root window
root =  tk.Tk()
root.geometry("450x250")
#root.resizable(False, False)
root.title('Register Machine')

# store user input
file_dir = tk.StringVar()

def deploy_contract():
    contract, address = deployContracts.compile_and_deploy_contract(
        newContractDetails.abi, 
        newContractDetails.bytecode
        )
    return contract, address

## 1. uploads machine file to ipfs
## 2. mints the returned hash as url
def register_machine_v1(contract, address, machine_file_path=""):

    machine_hash = ipfs.store_file(machine_file_path)

    mintNFTs.mint_nft(contract, machine_hash)

    set_machine_info(machine_hash)

    return machine_hash, contract, address

machine_contract, contract_address = deploy_contract()

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
    text='Click me', 
    command=lambda: register_machine_v1(machine_contract, contract_address, file_dir.get())
    )
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

set_contract_address(contract_address)
    
root.mainloop()
