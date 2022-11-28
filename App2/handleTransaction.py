from web3 import Web3
import json
from urllib.request import urlopen
import os
import sys

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

# get the NFTs a user owns
def getMyNFTs(w3):
    # w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
    # w3.eth.default_account = w3.eth.accounts[1]

    numOfBLK = w3.eth.get_block('latest')["number"]
    
    allContractAddress = list(set([
        w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"]
        for i in reversed(range(1, numOfBLK+1)) 
        if w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"] is not None 
    ]))
    
    myNFTs_data = []
    
    for ca in allContractAddress:
        contract = w3.eth.contract(address=ca, abi=cd.abi)
        
        # print("my nft ownerrrrr", contract.functions.getOwnerOfToken(1).call())
        
        ownedToken = [
            x for x in range(contract.functions.totalSupply().call())
            if contract.functions.getOwnerOfToken(x+1).call() == w3.eth.default_account 
        ]
        
        if ownedToken:
            
            for num in ownedToken:
                metadata = contract.functions.dataItems(num).call()[-1]
                # print(json.loads(urlopen(metadata).read())["image"])
                
                myNFTs_data.append(
                    NFTs(ca,
                        metadata,
                        json.loads(urlopen(metadata).read())["image"],
                        json.loads(urlopen(metadata).read())["name"],
                        json.loads(urlopen(metadata).read())["attributes"][0]["department"],
                        num + 1,
                        contract.functions.getOwnerOfToken(num+1).call(),
                    )
                )
                
    return sorted(myNFTs_data, key=lambda x: x.collection, reverse=True)
  