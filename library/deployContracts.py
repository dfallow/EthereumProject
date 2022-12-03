from web3 import Web3
#import newContractDetails

# test environment
#w3 = Web3(Web3.WebsocketProvider("ws://192.168.0.24:8540"))
w3 = Web3(Web3.EthereumTesterProvider())
#gethaddr = "http://127.0.0.1:8545"
#gethaddr = "://127.0.0.1:3334"

#w3 = Web3(Web3.HTTPProvider(gethaddr))
#w3 = Web3(Web3.HTTPProvider(gethaddr))
print("ISCONNECTED", w3.isConnected())

w3.eth.default_account = w3.eth.accounts[0]



def show_accounts():
    print(w3.eth.accounts)
    
def change_default_account(account):
    w3.eth.default_account = account
    return w3.eth.default_account

# compiles and deploys contract, returns contract address
def compile_and_deploy_contract(contract_abi, contract_bytecode, account):
    # default account deploys contract -> msg.sender
    #w3.eth.default_account = account
    compiled_contract = w3.eth.contract(
        abi=contract_abi, bytecode=contract_bytecode
    )

    print("COMPILED CONTRACT", compiled_contract)
    transaction_hash = compiled_contract.constructor().transact()

    transanction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)

    contract_address = transanction_receipt["contractAddress"]

    deployed_contract = w3.eth.contract(
        address=contract_address, abi=contract_abi
    )

    return deployed_contract, contract_address, transaction_hash, transanction_receipt


def compile_contract_with_accounts(
    contract_abi, 
    contract_bytecode, 
    contract_owner, 
    registered_account
    ):
    w3.eth.default_account = contract_owner
    compiled_contract = w3.eth.contract(
        abi=contract_abi, bytecode=contract_bytecode
    )

    transaction_hash = compiled_contract.constructor(registered_account).transact()

    transanction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)

    contract_address = transanction_receipt["contractAddress"]

    print("BEFORE")
    deployed_contract = w3.eth.contract(
        address=contract_address, abi=contract_abi
    )
    print("AFTER")
    print("DEPLOYED CONTRACT", deployed_contract)

    return deployed_contract, contract_address, transaction_hash, transanction_receipt