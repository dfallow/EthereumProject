import json
import os

import ipfsApi

api = ipfsApi.Client("127.0.0.1", 5001)


# creates new file in /tempFiles
def write_json(new_file, info_object, json_object, keys):

    with open(new_file, "x") as file:
        file.write(info_object)
    with open(new_file, "r+") as file:
        file_data = json.load(file)
        for i in range(0, keys):
            file_data[i]["directory"] = (
                "https://ipfs.io/ipfs/" +
                json_object[i]["directory"] + "/" +
                json_object[i]["name"]
            )
            i += 1
        file.seek(0)
        json.dump(file_data, file, indent=4)


def store_ipfs_file(file_name, info_object):
    new_dir = os.path.dirname(os.path.realpath(__file__))
    new_file = new_dir + "/tempFiles/" + file_name + ".json"
    print("NEW FILE", new_file)

    json_object = json.loads(info_object)
    keys = len(json_object)
    print("KEYS", keys)

    write_json(new_file, info_object, json_object, keys)

    # adds file to ipfs
    # res = api.add(new_file)
    # hash of the file on ipfs
    # hash = str(res[0]["Hash"])
    # url
    # url = "https://ipfs.io/ipfs/" + hash
    # return hash, url
    return "hash", "url"
