from web3 import Web3
import json
from urllib.request import urlopen
import os
import sys

sys.path.append(os.path.abspath(os.path.join('.')))
from App1 import newContractDetails as cd
from App2 import handleTransaction

def transferOwnerOfNFT(w3, tid, ca, to, key):
    from_user = w3.eth.default_account
    contract = w3.eth.contract(address=ca, abi=cd.abi)
    owner = contract.functions.getOwnerOfToken(int(tid)).call()
    print("PREVIOUS OWNER: ", owner)
    
    nft_transfer = contract.functions.transferTokenOwnership(from_user, to, int(tid)).buildTransaction(
        {
            'from': from_user,
            'gas': 1000000,
            'gasPrice': w3.toWei("70", "gwei"),
            'nonce': w3.eth.get_transaction_count(from_user),

        }
    )
    print("NFT TRANSFER BUILD: ", nft_transfer)
    
    signed_nft_transfer = w3.eth.account.sign_transaction(nft_transfer, key)
    
    print("SIGNED TRANSFER: ", signed_nft_transfer)
    
    signed_nft_transfer_txh = w3.eth.send_raw_transaction(signed_nft_transfer.rawTransaction)
    print("SIGNED TRANSFER HASH: ", signed_nft_transfer_txh)
    
    nft_transfer_receipt = w3.eth.wait_for_transaction_receipt(signed_nft_transfer_txh)
    print("NFT TRANSFER RECEIPT: ", nft_transfer_receipt)
    
    new_owner = contract.functions.getOwnerOfToken(int(tid)).call()
    print("NEW OWNER: ", new_owner)
    