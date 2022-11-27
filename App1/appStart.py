import os
import numpy as np
import mne
import glob
import ipfsApi
import deployMachineData

api = ipfsApi.Client("127.0.0.1", 5001)

# Selects .edf files from user input directory,
# converts them to .csv
def convert_files():

    edf_files = []

    print(os.getcwd())
    dir = input("Enter the directory: ")
    
    # Gets all .edf files from directory
    for file in glob.glob(dir + '*.edf'):
        edf_files.append(file)

    # Creates a target directory for .csv files
    if not os.path.exists(dir + 'csvFiles'):
        os.mkdir(dir + 'csvFiles')
        print("Directory", 'csvFiles', "Created")
    else:
        print("Directory", 'csvFiles', "Already Exists")

    # Converting .edf files into .csv
    for file in edf_files:
        print(edf_files.index(file))
        edf = mne.io.read_raw_edf(file)
        print(edf)
        header = ','.join(edf.ch_names)
        print(edf.ch_names)
        np.savetxt(dir + 'csvFiles/' + str(edf_files.index(file)) + '.csv', edf.get_data().T, delimiter=',', header=header)

    # Returns array of .csv files
    return glob.glob(dir + 'csvFiles/*.csv'), dir + 'csvFiles/'


# storing .csv files in ipfs
def store_files_ipfs(files):
    hash_array = []

    for file in files:
        res = api.add(file)
        hash = str(res[0]["Hash"])
        hash_array.append(hash)

    print("HASH ARRAY", hash_array)

    return hash_array

def upload_files():
    dataFiles, dir = convert_files()
    hashArray = store_files_ipfs(dataFiles)
    hash_array, url_array = deployMachineData.deploy_nfts_from_python(str(hashArray))


def register_machine():
    
    machine_file_dir = input("Enter Path to File: ")

    machine_data = {}

    print("Enter details about the machine --> tagName: tag")
    while(True):
        tag_name = input("Please enter tagName: ")
        if tag_name == "":
            break

        tag = input("Enter the tag: ")
        if tag == "":
            break

        machine_data[tag_name] = tag

        print("Enter more tags, or leave empty to finish")

    print("MACHINE DATA", machine_data)

    return

register_machine()
#upload_files()