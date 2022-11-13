import os
import IPFSv2
import newDeployNFT


def test_is_connected():
    assert newDeployNFT.is_connected(newDeployNFT.w3) is True


# def test_default_account():
#    deployNFT.w3.eth.default_account == deployNFT.w3.eth.accounts[0]


# test if file is saved correctly
# "image" in the final file should be changed from "12345" to a mock URL
def test_save_to_file():
    new_dir = os.path.dirname(os.path.realpath(__file__))
    file_name = "my_test_file"
    new_file = new_dir + "/tempFiles/" + file_name + ".json"

    # this is what is passed to write_json()
    info_object = '{ "image": "12345", "name": "test photo", "attributes": [{"department": "my department name"}]}'

    # this is what is expected to be in the final version of the file after write_json() manipulates it
    expected_content = '{\n    "image": "https://ipfs.io/ipfs/12345?12345",\n    "name": "test photo",\n    "attributes": [\n        {\n            "department": "my department name"\n        }\n    ]\n}'

    # create the file. If filename already exists, the test will fail
    assert (
        IPFSv2.write_json(new_file, info_object) is True
    ), "File wasn't saved. Filename already exists or other reason."

    # compare file contents with expected result
    assert open(new_file).read() == expected_content, "File contents don't match"

        


        
