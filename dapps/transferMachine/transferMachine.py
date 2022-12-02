import tkinter as tk
from tkinter import *
from library import deployContracts, contractDetailsMachine, variables, contractInteraction

# root window
root = tk.Tk()
root.geometry("450x450")
root.resizable(False, False)
root.title('Transfer Machine Ownership')

# store user input
doctor_account = tk.StringVar()
contract_address = tk.StringVar()
current_owner = tk.StringVar()


def deploy_machine_contract():

    contract, address, hash, receipt = deployContracts.compile_and_deploy_contract(
        contractDetailsMachine.abi,
        contractDetailsMachine.bytecode,
        deployContracts.w3.eth.accounts[0] # default account for demo
    )

    variables.machine_contract_var = contract
    contract_address.set(address)
    #current = deployContracts.w3.eth.accounts[0]
    current_owner.set(deployContracts.w3.eth.accounts[0])
    
    set_contract_address(contract_address.get())
    set_current_owner(current_owner.get())


    return

def transfer_machine():
    
    contractInteraction.transfer_machine(
        variables.machine_contract_var,
        
    )
    
    return





## Tkinter ##

# account input frame
accounts_frame = Frame(root)
accounts_frame.pack(padx=10, pady=10, fill='x')

# account to transfer to address
doctor_account_label = Label(accounts_frame, text="Enter Account To Transfer Machine To:")
doctor_account_label.pack(fill='x', expand=True)

doctor_account_entry = Entry(accounts_frame)
doctor_account_entry.pack(fill='x', expand=True)

# transfer to account
transfer_btn = Button(
    accounts_frame,
    text="Transfer Machine",
    command=transfer_machine
)
transfer_btn.pack(fill='x', expand=True, pady=10)

# current contract frame -> showes inforamtion about the deployed contract
owner_frame = Frame(root, height=20)
owner_frame.pack(padx=10, pady=10, fill='x')

# contract label
contract_label = Label(owner_frame, text="Current Contract Address:")
contract_label.pack(fill='x', expand=True)

# contract address
current_contract = Entry(owner_frame)
current_contract.pack(fill='x', expand=True)

# previous owner
previous_owner_label = Label(owner_frame, text="Previous Contract Owner:")
previous_owner_label.pack(fill='x', expand=True)

previous_owner = Entry(owner_frame)
previous_owner.pack(fill='x', expand=True)

# current owner
current_owner_label = Label(owner_frame, text="Current Contract Owner:")
current_owner_label.pack(fill='x', expand=True)

current_owner_entry = Entry(owner_frame)
current_owner_entry.pack(fill='x', expand=True)


def set_contract_address(address):
    current_contract.delete(0, END)
    current_contract.insert(0, address)

def set_previous_owner(address):
    previous_owner.delete(0, END)
    previous_owner.insert(0, address)
    
def set_current_owner(address):
    current_owner_entry.delete(0, END)
    current_owner_entry.insert(0, address)
    
deployContracts.show_accounts()
deploy_machine_contract()
    
root.mainloop()

