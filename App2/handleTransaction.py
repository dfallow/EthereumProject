from web3 import Web3
import json
from urllib.request import urlopen
import os
import sys

sys.path.append(os.path.abspath(os.path.join('..')))
from App1 import contractDetails as cd

def main(w3):
    # get latest block
    
    target_block = w3.eth.get_block(6)
    print("Block details: ", target_block)
    
    txh = target_block["transactions"][0].hex()
    print("Transaction hash: ", txh)
    
    # get transaction
    transaction = w3.eth.get_transaction(txh)
    print("Transaction details: ", transaction)
    
    c_add = transaction["to"]
    contract = w3.eth.contract(address=c_add, abi=cd.abi)
    
    numOfNFTs = contract.functions.totalSupply().call()
    
    print("number of NFTs in this collections", numOfNFTs)
        
    
    return [json.loads(urlopen(contract.functions.dataItems(i).call()[-1]).read())["image"]
        for i in range(numOfNFTs)]
        
    
    # print(contract.functions.dataItems(0).call())
    # print(contract.functions.dataItems(1).call())
    
    # print("OWNERSHIP", contract.functions.getOwnerOfToken(1).call() )
    # c_data = 
    # print(c_data)
    
    
    # metadata = json.loads(urlopen(c_data[-1]).read())
    # print("https://ipfs.io/ipfs/" + metadata["imageUrl"])
  
