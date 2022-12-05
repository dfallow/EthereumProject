import IPFSv2
import machineTokenABI
import json
from web3 import Web3

# test environment
# w3 = Web3(Web3.EthereumTesterProvider())
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

# deployed by manufacturer
# this is atm set to the available accounts
w3.eth.default_account = w3.eth.accounts[4]
print("ACCOUNTS", w3.eth.accounts)

# check if connected successfully
print("IS CONNECTED", w3.isConnected())

# can run when needed to check connection


def is_connected(w3):
    return w3.isConnected()


# compile contract
contract_compiled = w3.eth.contract(
    abi=machineTokenABI.abi, bytecode=machineTokenABI.bytecode
)
transaction_hash = contract_compiled.constructor().transact()
print("MACHINE CONTRACT TRANSACTION HASH", transaction_hash)
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
print("MACHINE CONTRACT TRANSACTION RECEIPT", transaction_receipt)

# retrieve contract address
contract_address = transaction_receipt["contractAddress"]
print("MACHINE CONTRACT ADDRESS", contract_address)

# deploy contract (creates an instance of a contract) with the address above
contract_deployed = w3.eth.contract(
    address=contract_address, abi=machineTokenABI.abi
)

token_id = 0


def deploy_machine_nft(file_hash):
    global token_id

    w3.eth.default_account = w3.eth.accounts[4]

    file_url = "https://ipfs.io/ipfs/" + file_hash + "?" + file_hash

    # mint NFT
    contract_deployed.functions.mint(file_url).transact()
    event = contract_deployed.events.Minted().getLogs()
    print("MINTED EVENT", event)
    token_id = event[0]["args"]["tokenId"]
    print("Machine TokenId", token_id)

    # get totalSupply(NFT count)
    print("NFT count", contract_deployed.functions.totalMachineTokens().call())

    print("BLOCK number", w3.eth.block_number)
