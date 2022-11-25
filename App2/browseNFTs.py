from web3 import Web3
import json
import os
import sys
from urllib.request import urlopen
import collections

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

def getAllNFTs(w3):
    
    # get the total number of blocks on the chain
    numOfBLK = w3.eth.block_number
    # print(numOfBLK)
    
    # get all valid contract address in the blockchain
    allContractAddress = list(set([
        w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"]
        for i in reversed(range(1, numOfBLK+1)) 
        if w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"] is not None 
    ]))
    # print(allContractAddress)
    
    # initialise a list
    NFTs_data = []
    
    for ca in allContractAddress:
        contract = w3.eth.contract(address=ca, abi=cd.abi)
        numOfNFTs = contract.functions.totalSupply().call()
        
        NFTs_data += [NFTs
             (ca,
              contract.functions.dataItems(n).call()[-1],
              json.loads(urlopen(contract.functions.dataItems(n).call()[-1]).read())["image"],
              json.loads(urlopen(contract.functions.dataItems(n).call()[-1]).read())["name"],
              json.loads(urlopen(contract.functions.dataItems(n).call()[-1]).read())["attributes"][0]["department"],
              n + 1,
              contract.functions.getOwnerOfToken(n+1).call()
            )for n in range(numOfNFTs)]
            
    return sorted(NFTs_data, key=lambda x: x.collection, reverse=True)

def getAllNFTsCollections(w3):
    
    numOfBLK = w3.eth.block_number
    
    ca_dict = collections.defaultdict(list)
    
    for i in reversed(range(1, numOfBLK+1)):
        if (w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"] not in ca_dict 
            and w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"] is not None):
            # ca_dict[w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"]] = True
            ca = w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"]
            contract = w3.eth.contract(address=ca, abi=cd.abi)
            ca_dict[ca].append(json.loads(urlopen(contract.functions.dataItems(0).call()[-1]).read())["image"])
            ca_dict[ca].append(json.loads(urlopen(contract.functions.dataItems(0).call()[-1]).read())["attributes"][0]["department"])
            
    
    return ca_dict
            
            
            
    
        
    
    
    
