import ipfsApi
import os

api = ipfsApi.Client('127.0.0.1', 5001)

def store_ipfs_file(file_name, info_object):

    print(__file__)
    new_dir = os.path.dirname(os.path.realpath(__file__))
    ##new_ipfs_file = new_dir + "/fileForIPFS.json"
    print(new_dir)

    ##new_file = new_dir + "/fileForIPFS.json"
    new_file = new_dir + "/tempFiles/" + file_name + ".json"

    ##creates new file in /tempFiles
    def write_json():
        with open(new_file, "x") as file:
            file.write(info_object)
            
    write_json()

    ## adds file to ipfs
    res = api.add(new_file)
    print(res)
    ##hash of the file on ipfs
    hash = str(res[0]['Hash'])
    ##url for convenience purpose
    url = "https://ipfs.io/ipfs/" + hash + "?" + hash
   
    return hash, url