import ipfsApi
import os

## Get current working directory
dir_path = os.getcwd()
print(dir_path)

try:
    ## Connecting to ipfs api
    api = ipfsApi.Client('127.0.0.1', 5001)
    ## setting filepath for directorty which the data is stored in
    file_path = dir_path +'/App1/'
    try:
        ## User inputs filename in terminal, this will be done automatically in future
        file_name = input("Enter file name : ")
        try:
            ## adds file to ipfs
            ## new_file contains 'Name', 'Hash', and 'Size'
            new_file = api.add(file_name)
            try:
                ## Save the information about the added file in own text file for reference
                file = open("save_data_address.txt", 'w')
                file.write(str(new_file) + "\n")
                file.write(str(new_file['Hash']))
            except:
                pass
        except:
            pass
    except: 
        pass
except ipfsApi.exceptions.ConnectionError as ce:
    print(str(ce))
