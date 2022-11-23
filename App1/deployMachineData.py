import IPFSv2
import newContractDetails
from web3 import Web3
import json

from newDeployNFT import w3

def create_files_to_store(name, files):
    files_array = files.split(",")

    print()
    print("FILE ARRAY", files_array)
    print("SINGLE FILE", files_array[0])
    for file in files_array:
        print("FILE INDEX", files_array.index(file))
        IPFSv2.store_ipfs_file_only_hash(name, file, files_array.index(file))
    return

def deploy_nfts(files_object):
    print()
    print()
    print("FILES", json.loads(files_object)['image'])
    print()
    print("here")
    print(json.loads(files_object)['name'],json.dumps(json.loads(files_object), indent=2))
    create_files_to_store(json.loads(files_object)['name'], json.loads(files_object)['image'])

    #create_files_to_store(json.loads(files_object['name']), json.loads(files_object['image']))
    
    return