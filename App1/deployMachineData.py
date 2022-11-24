import IPFSv2
import dataTokenABI
from web3 import Web3
import json

from newDeployNFT import w3

# compile contract
contract_compiled = w3.eth.contract(
    abi=dataTokenABI.abi, bytecode=dataTokenABI.bytecode
)

transaction_hash = contract_compiled.constructor(w3.eth.accounts[3]).transact()
print("DATA CONTRACT TRANSACTION HASH", transaction_hash)
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
print("DATA CONTRACT TRANSACTION RECEIPT", transaction_receipt)

# retrieve contract address
contract_address = transaction_receipt["contractAddress"]

# deploy contract (creates an instance of a contract) with the address above
contract_deployed = w3.eth.contract(
    address=contract_address, abi=dataTokenABI.abi
)


def create_files_to_store(name, files):
    files_array = files.split(",")

    files_hash_array = []
    files_url_array = []

    for file in files_array:
        # Store single file in ipfs
        file_hash, file_url = IPFSv2.store_ipfs_file_only_hash(
            name, file, files_array.index(file))
        files_hash_array.append(file_hash)
        files_url_array.append(file_url)
    return files_hash_array, files_url_array


def deploy_nfts(files_object):
    # returns two arrays which show the location in IPFS of each file
    hash_array, url_array = create_files_to_store(json.loads(
        files_object)['name'], json.loads(files_object)['image'])

    for url in url_array:
        contract_deployed.functions.mintDataToken(url).transact()
        event = contract_deployed.events.Minted().getLogs()
        print("MINTED EVENT", event)
        tokenId = event[0]["args"]["nftId"]
        print("NFT ID/TokenId", tokenId)

    print("BLOCK number", w3.eth.block_number)

    return
