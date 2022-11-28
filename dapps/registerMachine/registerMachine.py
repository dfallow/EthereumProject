import json
from library import ipfs

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

    machine_hash = ipfs.store_file(file)

    return machine_hash

# machine_file -> path to file
machine_hash = register_machine_v1()

