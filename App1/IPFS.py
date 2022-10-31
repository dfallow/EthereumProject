import ipfsApi
import os
import json

##with open('metaData.json') as file:
##    data = json.load(file)

##print(data)

##print(os.listdir())
dir_path = os.getcwd()
print(dir_path)

f = open(dir_path +'/App1/myfile.txt', "w")
f.write("I have created this file new")

import ipfshttpclient

##client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')

##res =client.add(f)
##print(res)


api = ipfsApi.Client('127.0.0.1', 5001)
res = api.add(f)
print(res)
f.close