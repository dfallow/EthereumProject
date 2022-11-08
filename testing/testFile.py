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

print(w3.eth.accounts)

gen_block = json.loads(w3.toJSON(w3.eth.get_block(0)))

print(gen_block)

contract_compiled = w3.eth.contract(
    abi=contractDetails.abi, bytecode=contractDetails.bytecode)

transaction_hash = contract_compiled.constructor().transact()
print("TRANSACTION HASH", transaction_hash)
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
print("TRANSACTION RECEIPT", transaction_receipt)

contract_address = transaction_receipt["contractAddress"]

print("BLOCKS BEFORE", w3.eth.get_block('latest'))

contract_deployed = w3.eth.contract(
    address=contract_address, abi=contractDetails.abi)

w3.eth.default_account = w3.eth.accounts[0]

cost = w3.toWei(0.5, 'ether')
gas_price = 1000000

buyer_txn = {'from': w3.eth.accounts[1], 'value': cost, 'gas': gas_price}

test = contract_deployed.all_functions()

print("FUNCTIONS", test)

mintable = contract_deployed.functions.isMintEnabled().call()

print("MINTING", mintable)

buyer_txn_hash = contract_deployed.functions.addDataItem(
    "test", "testURL").transact()

receipt = w3.eth.waitForTransactionReceipt(buyer_txn_hash)
print("RECEIPT", receipt)

print("BLOCKS After", w3.eth.get_block('latest'))

print(w3.eth.accounts)

print("DEFAULT", w3.eth.default_account)

#owner = contract_deployed.functions.getOwner().call()

# print(owner)

contract_deployed.functions.toggleIsMintEnabled().transact()

#print("MINT AFTER", contract_deployed.functions.isMintEnabled().call())

mint_tx = contract_deployed.functions.mint().transact()
print("TOKENID", mint_tx)
mint_receipt = w3.eth.waitForTransactionReceipt(mint_tx)
print("mint RECEIPT", mint_receipt)

print("ALL FUNCTIONS", contract_deployed.all_functions())
latestBlock = w3.eth.get_block('latest')
print("LATEST after minting", latestBlock)


owner = contract_deployed.functions.getOwnerOfToken(1).call()

print("BEFORE", owner)

test = contract_deployed.functions.changeOwnerOfToken(
    w3.eth.accounts[5], 1).transact()

print(test)
owner2 = contract_deployed.functions.getOwnerOfToken(1).call()

print("AFTER", owner2)

contract_owner = contract_deployed.functions.getOwner().call()
print("CONTRACT OWNER BEFORE", contract_owner)

contract_deployed.functions.changeOwnerOfContract(
    w3.eth.accounts[3]).transact()

contract_owner2 = contract_deployed.functions.getOwner().call()
print("CONTRACT OWNER AFTER", contract_owner2)

print("FINAL BLOCK NUMBER", w3.eth.block_number)
