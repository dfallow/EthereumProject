from web3 import Web3

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))


#returns the contracts on the blockchain of a particular type
def get_contracts(type, known_contract):
    
    matching_contracts = []
    matching_contract_addresses = []
    types = {}
    total_blocks = w3.eth.get_block('latest')["number"]
    
    for i in range(1, total_blocks+1):
        
        if (w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"] == None and w3.eth.get_transaction_receipt(w3.eth.get_block(i)["transactions"][0].hex())["contractAddress"] not in matching_contracts):
            
            # contract address
            ca = w3.eth.get_transaction_receipt(w3.eth.get_block(i)["transactions"][0].hex())["contractAddress"]
            matching_contract_addresses.append(ca)
            
            # bytecode
            bc = w3.eth.getTransaction(w3.eth.get_block(i)["transactions"][0].hex())["input"]
            
            bc_type = check_bytecode_type(type, bc, known_contract.bytecode)
            types[ca] = bc_type
            
            if bc_type == type:
                type_contract = w3.eth.contract(address=ca, abi=known_contract.abi)
                matching_contracts.append(type_contract)
                
                
                ## TODO
                tokens = type_contract.functions.totalMachineTokens().call()
                print("NUMBER OF TOKENS", tokens)
            else:
                tokens = 0
            
    return matching_contracts, matching_contract_addresses, types, tokens, total_blocks

def get_all_token_hashes(check_type, total_blocks):
    return [w3.eth.get_block(n)["transactions"][0].hex()
            for n in range(1, total_blocks+1)
            if w3.eth.get_transaction(w3.eth.get_block(n)["transactions"][0].hex())["to"] in check_type]
    
def get_nfts(check_type, total_blocks, contract_abi):
    
    all_token_hashs = get_all_token_hashes(check_type, total_blocks)
    
    print(w3.eth.getTransaction(all_token_hashs[0]))
    
    for token in all_token_hashs:
        transaction = w3.eth.getTransaction(token)
        ca = transaction["to"]
        c_type = check_type[transaction["to"]]
        
        current_contract = w3.eth.contract(address=ca, abi=contract_abi.abi)
    
        history = current_contract.decode_function_input(transaction.input)
        
        print("\n\nHISTORY", history[0])
        
    
    
    
    return

def check_bytecode_type(type, bc, known_bytecode):
    
    #print("\n\n\nBYTECODE", bc)
    #print("\n\n\nKNONW BC", known_bytecode)
    
    print("\n", bc == "0x" + known_bytecode)

    if bc == "0x" + known_bytecode:
        return type
    else:
        return ""