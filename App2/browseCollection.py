from web3 import Web3
import json
import os
import sys
from urllib.request import urlopen
import json

sys.path.append(os.path.abspath(os.path.join('.')))
from App1 import newContractDetails as cd

def getSmartContractCreator(w3, target_ca):
    
    numOfBLK = w3.eth.block_number
    
    # find first appearance the contract address
    for i in range(1, numOfBLK+1):
        if w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"] == target_ca:
            return w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["from"]
        

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


        
def getNFTsBySmartContract(w3, target_ca):
    # initialise a object list
    NFTs_data = []
    
    # access to the smart contract
    contract = w3.eth.contract(address=target_ca, abi=cd.abi)
    numOfNFTs = contract.functions.totalSupply().call()
    
    NFTs_data += [NFTs
             (target_ca,
              contract.functions.dataItems(n).call()[-1],
              json.loads(urlopen(contract.functions.dataItems(n).call()[-1]).read())["image"],
              json.loads(urlopen(contract.functions.dataItems(n).call()[-1]).read())["name"],
              json.loads(urlopen(contract.functions.dataItems(n).call()[-1]).read())["attributes"][0]["department"],
              n + 1,
              contract.functions.getOwnerOfToken(n+1).call()
            )for n in range(numOfNFTs)]
    
    return NFTs_data
    
    
    
    

