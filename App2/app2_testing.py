from web3 import Web3
import json
import os
import sys
from urllib.request import urlopen

sys.path.append(os.path.abspath(os.path.join('.')))
from App1 import newContractDetails as cd

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

w3.eth.default_account = w3.eth.accounts[0]
# print("current address:", w3.eth.default_account)

numOfBLK = w3.eth.block_number
# print("number of block here: ", numOfBLK)

ca = "0xbE18c6B024E037B12D1970e05472b6f7762ABed4"
contract = w3.eth.contract(address=ca, abi=cd.abi)

# for i in range(1, numOfBLK+1):
#     if w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"] == ca:
#         print(i)
#         break
# print(w3.eth.get_transaction(w3.eth.get_block(2)["transactions"][0].hex()))

# transfer_txh = w3.eth.get_block(2)["transactions"][0].hex()
# transfer_transaction = w3.eth.getTransaction(transfer_txh)
# print(transfer_transaction)
# # print(contract.decode_function_input(transfer_transaction.input)[0])

# mint_txh = w3.eth.get_block(2)["transactions"][0].hex()
# print(mint_txh)
# mint_receipt =  w3.eth.get_transaction_receipt(mint_txh)
# print(mint_receipt)
# print("who created the smart contract", mint_receipt["from"])
# print("when created the smart contract: block", mint_receipt["blockNumber"])
# print(mint_receipt["logs"][0]["address"])

print("\n")

# Minteds = contract.events.Minted().createFilter(fromBlock="0x0").get_all_entries()
# print(Minteds[-1])

# for i in Minteds:
#     print(i["event"], "x", i['args']["nftId"], "Null", i['args']["minter"])
# print("Event ", Minteds[-1]["event"])
# print("search after block ", Minteds[-1]["blockNumber"])

print("\n")

transfer_txh = w3.eth.get_block(33)["transactions"][0].hex()
print(w3.eth.get_transaction(transfer_txh)["to"])
transfer_transaction = w3.eth.getTransaction(transfer_txh)
print(transfer_transaction.input)
print(contract.decode_function_input(transfer_transaction.input)[0])
print(contract.decode_function_input(transfer_transaction.input)[1])
print(contract.decode_function_input(transfer_transaction.input)[1]['_from'])
print(contract.decode_function_input(transfer_transaction.input)[1]['_to'])
print(contract.decode_function_input(transfer_transaction.input)[1]['_tokenId'])






abi = w3.eth.getTransaction(w3.eth.get_block(2)["transactions"][0].hex())["input"]
# print(True if abi == "0x" + cd.bytecode else False)



Minteds = contract.events.Minted().createFilter(fromBlock="0x0").get_all_entries()
# print(Minteds)
# print(len(Minteds))
# print(Minteds[0]["args"]["minter"])

# print(contract.functions.dataItems(0).call())

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



