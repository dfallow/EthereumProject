from web3 import Web3;

import contractDetails;
import IPFS;

w3 = Web3(Web3.EthereumTesterProvider())

IPFS
print(IPFS.newFileTest)
Contract = w3.eth.contract(abi=contractDetails.abi, bytecode=contractDetails.bytecode)

print("Minting NFT")
tx_hash = Contract.constructor().transact()
print("TX HASH=", tx_hash,"\n")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("TX RECEIPT=", tx_receipt)