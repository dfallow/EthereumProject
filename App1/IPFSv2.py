import ipfsApi
import os
import json

api = ipfsApi.Client('127.0.0.1', 5001)

##used with filenames
counter = 1

def store_ipfs_file(file_name, info_object):
    print()
    print(file_name)
    print()
    global counter
    counter_ = counter

    name = "My new file" + str(counter_)

    print(__file__)
    new_dir = os.path.dirname(os.path.realpath(__file__))
    ##new_ipfs_file = new_dir + "/fileForIPFS.json"
    print(new_dir)

    ##new_file = new_dir + "/fileForIPFS.json"
    new_file = new_dir + "/tempFiles/" + file_name + ".json"

    ##override information that is currently in the json file
    def write_json():
        with open(new_file, "x") as file:
            file.write(info_object)
        ##with open(new_file, 'x+') as file:
        ##    file_data = json.load(file)
        ##    file_data["name"] = name
        ##    file_data["description"] = "This is a very descriptive description. woeigfg ewif"
        ##    ## "rewind" to the beginning of the document
        ##    file.seek(0)
        ##    json.dump(file_data, file, indent = 1)
            
    write_json()

    ## adds file to ipfs
    res = api.add(new_file)
    print(res)
    ##hash of the file on ipfs
    hash = str(res[0]['Hash'])
    ##url for convenience purpose
    url = "https://ipfs.io/ipfs/" + hash + "?" + hash
    ##update counter so that next file name would have a different number
    counter = counter + 1
    return hash, url