from web3 import Web3
from web3 import EthereumTesterProvider
import dataNFTdetails
import IPFSv2
import time
from threading import Thread

# create acc -> nft transaction to new acc -> minting

# test environment
w3 = Web3(EthereumTesterProvider())

# check if connected successfully
# print(w3.isConnected())

# inititalise a default test account
print(w3.eth.accounts)
w3.eth.default_account = w3.eth.accounts[0]
default_acc = w3.eth.default_account
print(f"Default account: {default_acc}")

# create my account
my_acc = w3.eth.account.create()
print(f"User's account: {my_acc.address}")

# insert ethereum from test acc to my account
tx_hash_init = w3.eth.send_transaction({
    'from': default_acc,
    'to': my_acc.address,
    'value': w3.toWei(5, 'ether')
})
# print(tx_hash_init)
w3.eth.get_transaction(tx_hash_init)
print(f"User's balance: {w3.fromWei(w3.eth.get_balance(my_acc.address), 'ether')} ETH")


# pass abi and bytecode from data generated through Remix
contract_compiled = w3.eth.contract(
    abi=dataNFTdetails.abi, bytecode=dataNFTdetails.bytecode)

transaction_hash = contract_compiled.constructor().transact()
print("TRANSACTION HASH: ", transaction_hash)
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
print("TRANSACTION RECEIPT: ", transaction_receipt)

# get contract's address
contract_address = transaction_receipt["contractAddress"]
print(f"CONTRACT ADDRESS: {contract_address}")
# deploy contract
# this creates a new block
contract_deployed = w3.eth.contract(address=contract_address, abi=dataNFTdetails.abi)
print(f"CONTRACT DEPLOYED: {contract_deployed}")


def addData():
    print("START")
    # add file to ipfs and retrieve file's hash and url
    file_hash, file_url = IPFSv2.store_ipfs_file()
    print(f"FILE HASH: {file_hash}")
    print(f"FILE URL: {file_url}")
    # add hash and url of the ipfs file to DataItem in the contract
    print(contract_deployed.functions.addDataItem(file_hash, file_url).call())
    # mint?
    print(contract_deployed.functions.mint().call())
    print("END")
    # print(contract_deployed.functions.totalNumOfNFT().transact())
    new_hash = contract_deployed.functions.addDataItem(file_hash, file_url).transact()
    new_receipt = w3.eth.wait_for_transaction_receipt(new_hash)
    print(new_receipt)


addData()
