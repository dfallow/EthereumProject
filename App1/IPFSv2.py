import json
import os
import ipfsApi

api = ipfsApi.Client("127.0.0.1", 5001)

#creating the files to store in IPFS
def write_json_only_hash(new_file, file_hash):
    print("FILE HASH", file_hash)

    file_json = {
        'image': "https://ipfs.io/ipfs/" + file_hash + "?" + file_hash,
        'name': "Machine Maybe"
    }

    with open(new_file, 'x') as file:
        file.write(json.dumps(file_json))


# creates new file in /tempFiles
def write_json(new_file, info_object):
    json_object = json.loads(info_object)
    with open(new_file, "x") as file:
        file.write(info_object)
    with open(new_file, "r+") as file:
        file_data = json.load(file)
        file_data["image"] = (
            "https://ipfs.io/ipfs/" + json_object["image"] + "?" + json_object["image"]
        )
        file.seek(0)
        json.dump(file_data, file, indent=4)


# for storing multiple files
def store_ipfs_file_only_hash(file_name, file_hash, file_index):
    new_dir = os.path.dirname(os.path.realpath(__file__))

    new_file = new_dir + "/tempFiles/" + file_name + str(file_index) + ".json"

    write_json_only_hash(new_file, file_hash)

    res = api.add(new_file)

    hash = str(res[0]["Hash"])

    url = "https://ipfs.io/ipfs/" + hash
    return hash, url


def store_ipfs_file(file_name, info_object):
    # print(__file__)
    new_dir = os.path.dirname(os.path.realpath(__file__))
    # new_ipfs_file = new_dir + "/fileForIPFS.json"
    # print(new_dir)

    # new_file = new_dir + "/fileForIPFS.json"
    new_file = new_dir + "/tempFiles/" + file_name + ".json"

    write_json(new_file, info_object)

    # adds file to ipfs
    res = api.add(new_file)
    # hash of the file on ipfs
    hash = str(res[0]["Hash"])
    # url
    url = "https://ipfs.io/ipfs/" + hash
    return hash, url
