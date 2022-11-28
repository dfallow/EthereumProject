import json
from ...library.ipfs import store_file

#from library import ipfs

def machine_user_input():
    
    machine_file_dir = input("Enter Path to File: ")

    res = api.add(machine_file_dir)
    hash = str(res[0]["Hash"])

    machine_data = {'image': hash}

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

    return json.dumps(machine_data)

def register_machine():

    machine_data = machine_user_input()

    print("HASH", machine_data)

    newDeployNFT.new_deploy_nft("test", machine_data)


def register_machine_v1():

    file = input("Enter Path to File: ")

    machine_hash = store_file(file) #ipfs in library

    return machine_hash

# machine_file of type file
# machine_info of type json
register_machine_v1()

# all_machine_info of type json, containing all information on machine
#register_machine_v2(all_machine_info)