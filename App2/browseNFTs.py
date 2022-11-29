from web3 import Web3
import json
import os
import sys
from urllib.request import urlopen

sys.path.append(os.path.abspath(os.path.join('.')))
from App1 import newContractDetails as cd

class NFTs:
    def __init__(
        self, contractAddress: str,
        ipfs_metadata: str,
        img_ipfs: str,
        name: str,
        collection: str,
        tokenId: int,
        owner: str,
    ):
        self.contractAddress = contractAddress
        self.ipfs_metadata = ipfs_metadata
        self.img_ipfs = img_ipfs
        self.name = name,
        self.collection = collection
        self.tokenId = tokenId
        self.owner = owner

def getAllNFTs():
    
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
    
    numOfBLK = w3.eth.get_block('latest')["number"]
    # print(numOfBLK)
    
    # get all valid contract address in the blockchain
    allContractAddress = list(set([
        w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"]
        for i in reversed(range(1, numOfBLK+1)) 
        if w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"] is not None 
    ]))
    # print(allContractAddress)
    
    NFTs_data = []
    
    for ca in allContractAddress:
        contract = w3.eth.contract(address=ca, abi=cd.abi)
        numOfNFTs = contract.functions.totalSupply().call()
    
        for num in range(numOfNFTs):
            
            metadata = contract.functions.dataItems(num).call()[-1]
            # imgIpfs = json.loads(urlopen(metadata).read())["image"]
            # collection = json.loads(urlopen(metadata).read())["attributes"][0]["department"]
            # name = json.loads(urlopen(metadata).read())["name"]
            # tid = num + 1
            # owner = contract.functions.tokenIdToOwner(tid).call()
            # print(json.loads(urlopen(metadata).read())["image"])

            NFTs_data.append(
                NFTs(ca,
                     metadata,
                     json.loads(urlopen(metadata).read())["image"],
                     json.loads(urlopen(metadata).read())["name"],
                     json.loads(urlopen(metadata).read())["attributes"][0]["department"],
                     num + 1,
                     contract.functions.tokenIdToOwner(num+1).call(),
                )
            )
            
            
    return NFTs_data
