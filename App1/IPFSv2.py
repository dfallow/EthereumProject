import ipfsApi
import os

api = ipfsApi.Client('127.0.0.1', 5001)

def store_ipfs_file(file_name, metadata):

    print(__file__)
    new_dir = os.path.dirname(os.path.realpath(__file__))
    ##new_ipfs_file = new_dir + "/fileForIPFS.json"
    print(new_dir)

    ##new_file = new_dir + "/fileForIPFS.json"
    new_metadata = new_dir + "/tempFiles/" + file_name + ".json"

    ##creates new file in /tempFiles
    def write_json():
        with open(new_metadata, "x") as file:
            file.write(metadata)
            
    write_json()

    ## adds file to ipfs
    res = api.add(new_metadata)
    print("META DATA:", res)
    ##hash of the file on ipfs
    hash = str(res[0]['Hash'])
    ##url for convenience purpose
    url = "https://ipfs.io/ipfs/" + hash + "?" + hash
   
    return hash, url