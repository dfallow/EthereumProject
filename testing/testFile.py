import json
import os
from web3 import Web3
from web3 import EthereumTesterProvider
import contractDetails
##import IPFSv2
import time
from threading import Thread
##from solcx import compile_standard, install_solc
# install_solc("0.8.4")


# current_dir = os.path.dirname(os.path.realpath(__file__))
# contract_path = current_dir + '/dataNFT.sol'

# with open(contract_path, 'r') as file:
#     contract_file = file.read()
#     print(contract_file)

# print(current_dir)

# compiled_solidity = compile_standard({
#     "language": "Solidity",
#     "sources": { "dataNFT.sol": {
#         "content": contract_file
#     }},
#     "settings": {
#         "outputSelection": {
#             "*": { "*":
#                 ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
#         }
#     }
# }, solc_version="0.7.0", allow_paths= ".")

# print("COMPILED SOLIDITY", compiled_solidity)


ganache_url = 'http://127.0.0.1:7545'
#w3 = Web3(Web3.HTTPProvider(ganache_url))
w3 = Web3(Web3.EthereumTesterProvider())

print(w3.isConnected())

#set default account
w3.eth.default_account = w3.eth.accounts[0]

#compile contract
contract_compiled = w3.eth.contract(
    abi=contractDetails.abi, bytecode=contractDetails.bytecode)

transaction_hash = contract_compiled.constructor("test hash", "test url").transact()
print("TRANSACTION HASH", transaction_hash)
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
print("TRANSACTION RECEIPT", transaction_receipt)

#retrieve contract address
contract_address = transaction_receipt["contractAddress"]

print("BLOCKS BEFORE", w3.eth.get_block('latest'))

#deploy contract (creates an instance of a contract) with the address above
contract_deployed = w3.eth.contract(
    address=contract_address, abi=contractDetails.abi)

print("BLOCK number", w3.eth.block_number)

print(contract_deployed.functions.dataItems(0).call())

#token owner before
print("TOKEN OWNER before", contract_deployed.functions.getOwnerOfToken(1).call())

#change token owner
contract_deployed.functions.changeOwnerOfToken(w3.eth.accounts[4], 1).transact()

#owner of token after
print("TOKEN OWNER after", contract_deployed.functions.getOwnerOfToken(1).call())

#contract owner
print(contract_deployed.functions.owner().call())

#change contract owner
print(contract_deployed.functions.transferOwnership(w3.eth.accounts[4]).transact())

#contract owner
print(contract_deployed.functions.owner().call())

print("BLOCK number", w3.eth.block_number)
