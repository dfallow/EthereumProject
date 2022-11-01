import ipfsApi
import os
import json

api = ipfsApi.Client('127.0.0.1', 5001)
counter = 1

def store_ipfs_file():
    global counter
    counter_ = counter
    ipfsFile = "./App1/fileForIpfs.json"

    name = "My new file" + str(counter_)

    def write_json():
        with open(ipfsFile, 'r+') as file:
            file_data = json.load(file)
            file_data["name"] = name
            file_data["description"] = "This is a very descriptive description."
            file.seek(0)
            json.dump(file_data, file, indent = 1)
            

    write_json()

    res_file = api.add(ipfsFile)
    print(res_file)

    fileMetaData = "./App1/filesMetaData.json"

    metaDataToUpload = {"name" : name,
                        "file_hash": res_file[0]["Hash"]}

    def write_meta_data(new_meta_data):
        with open(fileMetaData, 'r+') as meta_file:
            file_data = json.load(meta_file)
            file_data["meta_data"].append(new_meta_data)
            meta_file.seek(0)
            json.dump(file_data, meta_file, indent = 4)

    write_meta_data(metaDataToUpload)

    res_meta = api.add(fileMetaData)
    counter = counter + 1

store_ipfs_file()