import os
import json
import tkinter as tk
from tkinter import *
from library import ipfs


#root window
root = tk.Tk()
root.geometry("450x250")
root.resizable(False, False)
root.title('Upload Machine Files')

# store user input
# TODO add account here
directory = tk.StringVar()
machine_hash = tk.StringVar()


def upload_files_from_machine(machine, dir):

    file_from_directory = os.listdir(dir)
    file_hash_array = []

    dir_path = os.path.dirname(os.path.realpath(__file__))

    if os.path.exists(dir_path + '/files'):
        print("Directory Already Exists")
    else:
        os.mkdir(dir_path + '/files')
        print("Directory Created")

    print("DIR PATH", dir_path)
    # store each file in ipfs
    for file_to_add in file_from_directory:
        print("FILE", file_to_add)
        file_hash = ipfs.store_file(dir + file_to_add)
        file_hash_array.append(file_hash)

        json_info = {
            'fileHash': file_hash,
            'fileUrl': "https://ipfs.io/ipfs/" + file_hash,
            'machine_hash': machine.get()
        }

        json_file = json.dumps(json_info)
        file_path = dir_path + "/files/dataFile" + str(file_from_directory.index(file_to_add)) + ".json"
        new_file = open(file_path, "x")
        new_file.write(json_file)
        new_file.close()

        # TODO place this at the end
        os.remove(file_path)
    print("FILE ARRAY", file_hash_array)    



    ## TODO create json files containing file_hash and machine

    ## TODO store json files in ipfs

    ## TODO mint the returned hashes 
        
    return


## Tkinter ##

# frame
file_frame = Frame(root)
file_frame.pack(padx=10, pady=10, fill='x', expand=True)

# registered machine
machine_label = Label(file_frame, text="Enter Hash of Machine")
machine_label.pack(fill='x', expand=True)

machine_input = Entry(file_frame, textvariable=machine_hash)
machine_input.pack(fill='x', expand=True)

# user directory input
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