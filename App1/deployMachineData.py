import IPFSv2
import newContractDetails
from web3 import Web3
import json

from newDeployNFT import w3

def create_files_to_store(name, files):
    files_array = files.split(",")

    files_hash_array = []
    files_url_array = []

    for file in files_array:
        #Store single file in ipfs
        file_hash, file_url = IPFSv2.store_ipfs_file_only_hash(name, file, files_array.index(file))
        files_hash_array.append(file_hash)
        files_url_array.append(file_url)
    return files_hash_array, files_url_array

def deploy_nfts(files_object):
    #returns two arrays which show the location in IPFS of each file
    hash_array, url_array = create_files_to_store(json.loads(files_object)['name'], json.loads(files_object)['image'])

    print("HASHES", hash_array)
    print("URLs", url_array)    
    return