from web3 import Web3
import json
from urllib.request import urlopen
import os
import sys

sys.path.append(os.path.abspath(os.path.join('.')))
from App1 import newContractDetails as cd
from App2 import handleTransaction

def transferOwnerOfNFT(w3, tid, ca, to):
    from_user = w3.eth.default_account
    contract = w3.eth.contract(address=ca, abi=cd.abi)
    owner = contract.functions.getOwnerOfToken(int(tid)).call()
    print("OWNERRRRRRRRRRRRRRRRRRRRRRRRRRRR", owner)
    nft_transfer_txh = contract.functions.transferTokenOwnership(from_user, to, int(tid)).transact()
    print("NFT TRANSACTION", nft_transfer_txh)
    nft_transfer_receipt = w3.eth.wait_for_transaction_receipt(nft_transfer_txh)
    print("TRANSACTION RECEIPT", nft_transfer_receipt)