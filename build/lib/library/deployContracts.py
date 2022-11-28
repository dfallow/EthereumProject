from web3 import Web3
import contracts.contractDetails.newContractDetails as contract
# test environment
#w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
w3 = Web3(Web3.EthereumTesterProvider())

w3.eth.default_account = w3.eth.accounts[0]


# compiles contract for passed abi and bytecode
def compile_contract(contract_abi, contract_bytecode):
    compiled_contract = w3.eth.contract(
        abi=contract_abi, bytecode=contract_bytecode
    )

    return compile_contract

test = compile_contract(contract.abi, contract.bytecode)

print("CONTRACT", test)