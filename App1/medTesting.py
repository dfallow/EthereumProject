from web3 import Web3
import json
import os
import sys
from urllib.request import urlopen

sys.path.append(os.path.abspath(os.path.join('.')))
from App1 import machineTokenABI as mta
from App1 import patientTokenABI as pta
from App1 import prescriptionTokenABI as preta
from App1 import dataTokenABI as dta

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

w3.eth.default_account = w3.eth.accounts[1]

caToBytecode = {}

numOfBLK = w3.eth.block_number
# print(numOfBLK)

# for n in range(1, numOfBLK+1):
#     if (w3.eth.get_transaction(w3.eth.get_block(n)["transactions"][0].hex())["to"] == None and
#     w3.eth.get_transaction_receipt(w3.eth.get_block(n)["transactions"][0].hex())["contractAddress"] not in caToBytecode):
#         ca = w3.eth.get_transaction_receipt(w3.eth.get_block(n)["transactions"][0].hex())["contractAddress"]
#         bc = w3.eth.getTransaction(w3.eth.get_block(n)["transactions"][0].hex())["input"]
#         #print("\nBC", bc )
#         caToBytecode[ca] = bc
        
# # print(preta.bytecode)

# for i in caToBytecode:
#     print(i)
#     if caToBytecode[i] == "0x" + mta.bytecode:
#         print("machine")
#     elif caToBytecode[i] == "0x" + pta.bytecode:
#         print("patient")
#     elif caToBytecode[i][:(len(caToBytecode[i])-64)] == "0x" + preta.bytecode:
#         print("prescription")
#     elif caToBytecode[i][:(len(caToBytecode[i])-64)] == "0x" + dta.bytecode:
#         print("data")
        

allValidTxh = [w3.eth.get_block(n)["transactions"][0].hex() for n in range(1, numOfBLK+1)]

txh = w3.eth.getTransaction(allValidTxh[2])
print(txh["hash"].hex())
print(txh["blockNumber"])
print(txh["from"])
# print(txh["to"])


ca = "0x4033c8e18773A11a5f97112551a102C77BaA30a8"

contract = w3.eth.contract(address=ca, abi=mta.abi)

history = contract.decode_function_input(txh.input)

print(history)

print(history[1]['_to'])
        
    

    

