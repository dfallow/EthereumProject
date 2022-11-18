from web3 import Web3
import json
from urllib.request import urlopen
import os
import sys

sys.path.append(os.path.abspath(os.path.join('.')))
from App1 import newContractDetails as cd

def transferOwnerOfNFT(w3, tid, ca, to):
    w3.eth.default_account = w3.eth.accounts[1]
    contract = w3.eth.contract(address=ca, abi=cd.abi)
    nft_transfer_txh = contract.functions.changeOwnerOfToken(to, int(tid)).transact()
    print("NFT TRANSACTION", nft_transfer_txh)
    nft_transfer_receipt = w3.eth.wait_for_transaction_receipt(nft_transfer_txh)
    print("TRANSACTION RECEIPT", nft_transfer_receipt)