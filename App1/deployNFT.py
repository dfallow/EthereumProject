from web3 import Web3
from web3 import EthereumTesterProvider
import dataNFTdetails
import IPFSv2

## test environment
w3 = Web3(EthereumTesterProvider())

## check if connected successfully
print(w3.isConnected())

## pass abi and bytecode from data generated through Remix
contract_compiled = w3.eth.contract(abi=dataNFTdetails.abi, bytecode=dataNFTdetails.bytecode)

## store file on IPFS and return it's hash and url
##ipfs daemon has to be running in the terminal
file_hash = IPFSv2.store_ipfs_file()
##second value is a url that displayes the file. Currently, it's just a json file.
print("FILE1 on IPFS", file_hash)
transaction_hash = contract_compiled.constructor().transact()  ##contract deployed
print("TRANSACTION HASH", transaction_hash)
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
print("TRANSACTION RECEIPT", transaction_receipt)
contract_deployed = w3.eth.contract(address=transaction_receipt["contractAddress"], abi=dataNFTdetails.abi)
print(contract_deployed)
res = contract_deployed.functions.addDataItem("test", "test").call()
print(res)
res2 = contract_deployed.functions.getDataItems().call()
print(res2)