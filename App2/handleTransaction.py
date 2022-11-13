from web3 import Web3
import json
from urllib.request import urlopen
import os
import sys

sys.path.append(os.path.abspath(os.path.join('..')))
from App1 import contractDetails as cd

def main(w3):
    # get latest block
    txh = w3.eth.get_block('latest')["transactions"][0].hex()
    print(txh)
    # get transaction
    transaction = w3.eth.get_transaction(txh)
    print(transaction)
    # contract address
    c_add = transaction["to"]
    print(c_add)
    contract = w3.eth.contract(
        address=c_add, abi=cd.abi)
    print("OWNERSHIP", contract.functions.getOwnerOfToken(1).call() )
    c_data = contract.functions.dataItems(0).call()
    print(c_data)
    
    metadata = json.loads(urlopen(c_data[-1]).read())
    print("https://ipfs.io/ipfs/" + metadata["imageUrl"])
  
