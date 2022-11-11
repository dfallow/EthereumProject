import ipfsApi
import os
import json

api = ipfsApi.Client('127.0.0.1', 5001)


def store_ipfs_file(file_name, info_object):
    json_object = json.loads(info_object)

    print(__file__)
    new_dir = os.path.dirname(os.path.realpath(__file__))
    ##new_ipfs_file = new_dir + "/fileForIPFS.json"
    print(new_dir)

    ##new_file = new_dir + "/fileForIPFS.json"
    new_file = new_dir + "/tempFiles/" + file_name + ".json"

    # creates new file in /tempFiles
    def write_json():
        with open(new_file, "x") as file:
            file.write(info_object)
        with open(new_file, "r+") as file:
            file_data = json.load(file)
            file_data["image"] = "https://ipfs.io/ipfs/" + \
                json_object["image"] + "?" + json_object["image"]
            file.seek(0)
            json.dump(file_data, file, indent=1)
    write_json()

    # adds file to ipfs
    res = api.add(new_file)
    print(res)
    # hash of the file on ipfs
    hash = str(res[0]['Hash'])
    # url for convenience purpose
    url = "https://ipfs.io/ipfs/" + hash

    return hash, url
