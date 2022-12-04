import tkinter as tk
from tkinter import *
from library import deployContracts, variables, contractInteraction, getContracts
from library import contractDetailsMachine as machine_cd
from library import contractDetailsMachineData as data_cd
from library import contractDetailsPatientToken as patient_cd
from library import contractDetailsPrescription as prescription_cd


# root window
root = tk.Tk()
root.geometry("400x500")
root.title("Get NFTs From Blockchain")

# store user input
input_user_account = tk.StringVar()
contract_type = tk.StringVar()

def get_all_contract_address_on_block():
    
    
    contracts, contract_addresses, check_type, number_of_tokens, total_blocks = getContracts.get_contracts("data", data_cd)
    
    print("\n\nADDRESSES", contracts)
    
    print("CONTRACT FUNCTIONS", contracts[0].functions)
    
    test = getContracts.get_nfts(check_type, total_blocks, machine_cd)
    
    print("TEST", test)
    
    
    #getContracts.check_contracts(contract_addresses)
    
    return

def get_selected_item():
    for i in list.curselection():
        print(list.get(i))
        contract_type.set(list.get(i))



get_all_contract_address_on_block()

# user input frame
user_input = Frame(root)
user_input.pack(side=LEFT, fill='x', padx=10, pady=10, expand=True)

# user account input
user_account_label = Label(user_input, text="Enter User Account")
user_account_label.pack(fill='x')

user_account_entry = Entry(user_input, textvariable=input_user_account)
user_account_entry.pack(fill='x')

list = Listbox(user_input, selectmode="single", height=0)
list.pack()

x = ["machine", "data", "patient", "prescription"]

for each_item in range(len(x)):

    list.insert(END, x[each_item])
    
    
find_contract = Button(
    user_input,
    text="Find Contract",
    command=get_selected_item
)
find_contract.pack(fill='x', pady=10)
    

root.mainloop()