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
    print(allContractAddress)
    
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
