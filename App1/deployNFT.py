from web3 import Web3
from web3 import EthereumTesterProvider
import dataNFTdetails
import IPFSv2
import time
from threading import Thread

# test environment
w3 = Web3(EthereumTesterProvider())

# check if connected successfully
print(w3.isConnected())

# pass abi and bytecode from data generated through Remix
contract_compiled = w3.eth.contract(
    abi=dataNFTdetails.abi, bytecode=dataNFTdetails.bytecode)

# compile contract
transaction_hash = contract_compiled.constructor().transact()
print("TRANSACTION HASH", transaction_hash)
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
print("TRANSACTION RECEIPT", transaction_receipt)

# get contract's address
contract_address = transaction_receipt["contractAddress"]
# deploy contract
# this creates a new block
contract_deployed = w3.eth.contract(
    address=contract_address, abi=dataNFTdetails.abi)


def addData():
    print("START")
    # add file to ipfs and retrieve file's hash and url
    file_hash, file_url = IPFSv2.store_ipfs_file()
    # add hash and url of the ipfs file to DataItem in the contract
    print(contract_deployed.functions.addDataItem(file_hash, file_url).call())
    # mint?
    print(contract_deployed.functions.mint().call())
    print("END")


addData()
