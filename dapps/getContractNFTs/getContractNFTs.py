import tkinter as tk
from tkinter import *
from library import getContracts
from library import contractDetailsMachine as machine_cd
from library import contractDetailsMachineData as data_cd
from library import contractDetailsPrescription as prescription_cd


# root window
root = tk.Tk()
root.geometry("1600x500")
root.title("Get History From Blockchain")

# store user input
input_user_account = tk.StringVar()

def get_contract_history():
    
    delete()

    type = get_selected_item()
    
    selected_contract = {
        'machine': machine_cd,
        'data': data_cd,
        'prescription': prescription_cd
    }
    
    contracts, check_type, total_blocks = getContracts.get_contracts(type, selected_contract[type])
    
    print("\n\nADDRESSES", check_type)
    
    print("CONTRACT FUNCTIONS", contracts)
    
    all_history = getContracts.get_nfts(contracts,check_type, total_blocks)
    
    print("TEST", all_history)
    
    for item in all_history:
        #insert_into_text(str(item))
        nfts_text_box.insert(INSERT, str(item) + "\n")
   

    return

def get_selected_item():
    for i in list.curselection():
        print(list.get(i))
        return list.get(i)


# user input frame
user_input = Frame(root)
user_input.pack(side=LEFT, fill='x', padx=10, pady=10, expand=True)

list = Listbox(user_input, selectmode="single", height=0)
list.pack()

x = ["machine", "data", "prescription"]

for each_item in range(len(x)):

    list.insert(END, x[each_item])
    
    
find_contract = Button(
    user_input,
    text="Get Contract History",
    command=get_contract_history
)
find_contract.pack(fill='x', pady=10)

nfts_text_box = Text(user_input)
nfts_text_box.pack(fill='x', pady=10)
    
    
def delete():
    nfts_text_box.delete('1.0', END)

root.mainloop()