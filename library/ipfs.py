import ipfsApi

api = ipfsApi.Client("127.0.0.1", 5001)

def store_file(file):

    #add file to ipfs
    res = api.add(file)
    # hash of file stored in ipfs
    file_hash = str(res[0]["Hash"])
    
    return file_hash