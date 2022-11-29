import easygui
from library import ipfs, deployContracts, newContractDetails, mintNFTs

import tkinter as tk
from tkinter import *

# root window
root =  tk.Tk()
root.geometry("300x150")
root.resizable(False, False)
root.title('Register Machine')


def deploy_contract():
    contract, address = deployContracts.compile_and_deploy_contract(
        newContractDetails.abi, 
        newContractDetails.bytecode
        )
    return contract, address


## 1. uploads machine file to ipfs
## 2. mints the returned hash as url
def register_machine_v1(contract, address, machine_file_path=""):

    print("FILE DIR", file_dir.get())

    if machine_file_path == "":
        machine_file_path = easygui.enterbox("Test?")

    machine_hash = ipfs.store_file(machine_file_path)

    mintNFTs.mint_nft(contract, machine_hash)

    return machine_hash, contract, address

machine_contract, contract_address = deploy_contract()

# store user input
file_dir = tk.StringVar()

# file directory
directory_label = Label(root, text="Enter Path to Machine File")
directory_entry = Entry(root, textvariable=file_dir)

button = Button(
    root, 
    text='Click me', 
    command=lambda: register_machine_v1(machine_contract, contract_address, file_dir.get())
    )

directory_label.pack(fill='x', expand=True)
directory_entry.pack(fill='x', expand=True)
button.pack()

root.mainloop()
