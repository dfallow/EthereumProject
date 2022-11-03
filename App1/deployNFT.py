from web3 import Web3
from web3 import EthereumTesterProvider
import contractDetails
import IPFSv2

def deploy_nft():
    ## test environment
    w3 = Web3(EthereumTesterProvider())

    ## check if connected successfully
    print(w3.isConnected())

    ## pass abi and bytecode from data generated through Remix
    contract = w3.eth.contract(abi=contractDetails.abi, bytecode=contractDetails.bytecode)

    ## store file on IPFS and return it's hash and url
    ##ipfs daemon has to be running in the terminal
    file_hash = IPFSv2.store_ipfs_file()
    ##second value is a url that displayes the file. Currently, it's just a json file.
    print("FILE1 on IPFS", file_hash)
    transaction_hash = contract.constructor().transact()
    print("TRANSACTION HASH", transaction_hash)
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    print("TRANSACTION RECEIPT", transaction_receipt)

    ## repeats this two more times
    ## files are stored with different names, thus also have different hashes
    file_hash2 = IPFSv2.store_ipfs_file()
    print("FILE2 on IPFS", file_hash2)
    transaction_hash = contract.constructor().transact()
    print("TRANSACTION HASH", transaction_hash)
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    print("TRANSACTION RECEIPT", transaction_receipt)

    file_hash3 = IPFSv2.store_ipfs_file()
    print("FILE3 on IPFS", file_hash3)
    transaction_hash = contract.constructor().transact()
    print("TRANSACTION HASH", transaction_hash)
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    print("TRANSACTION RECEIPT", transaction_receipt)

    ##wasn't able to pass the file hash or url to the smart contract mint() function. 
    ##perhaps it should be a setTokenUri function instead
    """ first_nft_contract = w3.eth.contract(address=transaction_receipt["contractAddress"], abi=contractDetails.abi)
    file_hash = IPFS_v2.store_ipfs_file()
    print("FILEHASH1", file_hash)
    nft = first_nft_contract.functions.mint().call()
    print("NFT tokenId", nft) """
