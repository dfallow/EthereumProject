from web3 import Web3
import json
import os
import sys
from urllib.request import urlopen

sys.path.append(os.path.abspath(os.path.join('.')))
from App1 import newContractDetails as cd

class Activity:
    def __init__(
        self, event: str,
        item: str,
        tid: int,
        _from: str,
        _to: str,
    ):
        self.event = event,
        self.item = item,
        self.tid = tid,
        self._from = _from,
        self._to = _to,
        


    
async def getCollectionActivity(w3, ca, nft_data):
    
    # initialise a list to return it to html
    activity_data = []
    
    # get to know total number of blocks on the chain
    numOfBLK = w3.eth.block_number
    
    # provide access to the smart contract
    contract = w3.eth.contract(address=ca, abi=cd.abi)
    
    # firstly get all the "Minted" activity
    Minteds = contract.events.Minted().createFilter(fromBlock="0x0").get_all_entries()
    print(Minteds)
    
    for item in Minteds:
        activity_data.append(Activity(
            item["event"],
            nft_data[item["args"]["nftId"]-1].name,
            item["args"]["nftId"],
            "NullAddress",
            item["args"]["minter"]
        ))
        
    # next step get all transaction history if possible
    # search block after last minted item
    nextBLK = Minteds[-1]["blockNumber"]
    
    allValidTxh = [w3.eth.get_block(n)["transactions"][0].hex()
                   for n in range(nextBLK, numOfBLK+1)
                   if w3.eth.get_transaction(w3.eth.get_block(n)["transactions"][0].hex())["to"] == ca]
    
    for txh in allValidTxh:
        transfer_transaction = w3.eth.getTransaction(txh)
        history = contract.decode_function_input(transfer_transaction.input)
        
        if "transferTokenOwnership" in str(history[0]):
            activity_data.append(Activity(
                "Transfer",
                nft_data[contract.decode_function_input(transfer_transaction.input)[1]['_tokenId']-1].name,
                history[1]['_tokenId'],
                history[1]['_from'],
                history[1]['_to']
            ))

    return activity_data
    