from web3 import Web3
import json
from urllib.request import urlopen
import os
import sys

sys.path.append(os.path.abspath(os.path.join('.')))
from App1 import newContractDetails as cd

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

w3.eth.default_account = w3.eth.accounts[0]
# print("current address:", w3.eth.default_account)

numOfBLK = w3.eth.block_number
# print("number of block here: ", numOfBLK)

ca = "0x9aEa64E24096665d5223B809FFBcE5eb01Aa948d"
contract = w3.eth.contract(address=ca, abi=cd.abi)

print(contract.functions.dataItems(0).call())

# print all the blocks
# for i in range(2, numOfBLK+1):
#     # print(w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex()))
#     print(w3.eth.get_transaction_by_block(i, 0))
#     print("\n")




# mint_txh = w3.eth.get_block(4)["transactions"][0].hex()
# mint_receipt =  w3.eth.get_transaction_receipt(mint_txh)
# print(contract.events.Minted().processReceipt(mint_receipt))
# print("\n")

# transfer_txh = w3.eth.get_block(8)["transactions"][0].hex()
# transfer_transaction = w3.eth.getTransaction(transfer_txh)
# # print(transfer_transaction.input)
# print(contract.decode_function_input(transfer_transaction.input)[0])
# print(contract.decode_function_input(transfer_transaction.input)[1])
# print(contract.decode_function_input(transfer_transaction.input)[1]["_from"])
# print(contract.decode_function_input(transfer_transaction.input)[1]["_to"])
# print(contract.decode_function_input(transfer_transaction.input)[1]["_tokenId"])
# print(type(contract.decode_function_input(transaction.input)[1]))



