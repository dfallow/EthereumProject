from web3 import Web3

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))


#returns the contracts on the blockchain of a particular type
def get_contracts(type, known_contract):
    
    matching_contracts = []
    total_blocks = w3.eth.get_block('latest')["number"]
    
    for i in range(1, total_blocks+1):
        
        if (w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"] == None and w3.eth.get_transaction_receipt(w3.eth.get_block(i)["transactions"][0].hex())["contractAddress"] not in matching_contracts):
            
            # contract address
            ca = w3.eth.get_transaction_receipt(w3.eth.get_block(i)["transactions"][0].hex())["contractAddress"]
            
            # bytecode
            bc = w3.eth.getTransaction(w3.eth.get_block(i)["transactions"][0].hex())["input"]
            
            bc_type = check_bytecode_type(type, bc, known_contract.bytecode)
            
            if bc_type == type:
                type_contract = w3.eth.contract(address=ca, abi=known_contract.abi)
                matching_contracts.append(type_contract)
            
    return matching_contracts

def check_bytecode_type(type, bc, known_bytecode):
    
    #print("\n\n\nBYTECODE", bc)
    #print("\n\n\nKNONW BC", known_bytecode)
    
    print("\n", bc == "0x" + known_bytecode)

    if bc == "0x" + known_bytecode:
        return type
    else:
        return ""

def get_addresses():
    block = w3.eth.get_block('latest')
    print("\n\n\n", block)
    
    
    all_addresses = list(set([
        w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"]
        for i in reversed(range(1, block["number"]))
        if w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"] is not None
    ]))
    
    print("\n\n\n", all_addresses)
    
    
    return all_addresses

def check_contracts(addresses):
    
    for ca in addresses:
        contract = w3.eth.contract(address=ca, abi=cd.abi)
    
    return