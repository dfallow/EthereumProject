from web3 import Web3
from web3 import EthereumTesterProvider
import contractDetails
import IPFSv2
import json
import os
from web3 import Web3
from web3 import EthereumTesterProvider
import newContractDetails


def new_deploy_nft(file_name, info_object):
    # test environment
    w3 = Web3(EthereumTesterProvider())

    # check if connected successfully
    print("IS CONNECTED", w3.isConnected())

    # compile contract
    contract_compiled = w3.eth.contract(
        abi=newContractDetails.abi, bytecode=newContractDetails.bytecode)

    transaction_hash = contract_compiled.constructor().transact()
    print("TRANSACTION HASH", transaction_hash)
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    print("TRANSACTION RECEIPT", transaction_receipt)

    # store file on IPFS and return it's hash and url
    # ipfs daemon has to be running in the terminal
    file_hash, file_url = IPFSv2.store_ipfs_file(file_name, info_object)

    # set default account
    w3.eth.default_account = w3.eth.accounts[0]

    # retrieve contract address
    contract_address = transaction_receipt["contractAddress"]

    # deploy contract (creates an instance of a contract) with the address above
    contract_deployed = w3.eth.contract(
        address=contract_address, abi=contractDetails.abi)

    # save data and create nft
    contract_deployed.functions.safeDataItem(file_hash, file_url).transact()

    print("BLOCK number", w3.eth.block_number)
