from web3 import Web3
import contracts.contractDetails.newContractDetails as contract

# test environment
#w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
w3 = Web3(Web3.EthereumTesterProvider())

w3.eth.default_account = w3.eth.accounts[0]


# compiles and deploys contract, returns contract address
def compile_and_deploy_contract(contract_abi, contract_bytecode):
    compiled_contract = w3.eth.contract(
        abi=contract_abi, bytecode=contract_bytecode
    )

    transaction_hash = compiled_contract.constructor().transact()

    transanction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)

    contract_address = transanction_receipt["contractAddress"]

    deployed_contract = w3.eth.contract(
        address=contract_address, abi=contract_abi
    )

    return deployed_contract, contract_address

dep_contract, address = compile_and_deploy_contract(contract.abi, contract.bytecode)

print("CONTRACT", address)