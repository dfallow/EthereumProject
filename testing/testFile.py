import json
import os
from web3 import Web3
from web3 import EthereumTesterProvider
import contractDetails

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

#check if data was added to dataItems array
print(contract_deployed.functions.dataItems(0).call())

#NFT owner before
print("NFT OWNER before", contract_deployed.functions.getOwnerOfToken(1).call())

#change NFT owner
contract_deployed.functions.changeOwnerOfToken(w3.eth.accounts[4], 1).transact()

#owner of NFT after
print("NFT OWNER after", contract_deployed.functions.getOwnerOfToken(1).call())

#contract owner
print("CONTRACT OWNER", contract_deployed.functions.owner().call())

#change contract owner
contract_deployed.functions.transferOwnership(w3.eth.accounts[4]).transact()

#contract owner
print("CONTRACT OWNER",contract_deployed.functions.owner().call())

print("BLOCK number", w3.eth.block_number)
