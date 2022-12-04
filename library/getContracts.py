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
            
            print("\n\n\nTESTING", w3.eth.getTransaction(w3.eth.get_block(i)["transactions"][0].hex()))
            
            # bytecode
            bc = w3.eth.getTransaction(w3.eth.get_block(i)["transactions"][0].hex())["input"]
            
            print("\nBERFORE CHECK\n")
            bc_type = check_bytecode_type(type, bc, known_contract.bytecode)
            if bc_type == type:
                types[ca] = bc_type
            
            print("\nAFTER CHECK\n")
            
            print("\n\n bc type", bc_type == bc)
            
            if bc_type == type:
                type_contract = w3.eth.contract(address=ca, abi=known_contract.abi)
                matching_contracts.append(type_contract)
                
                
                ## TODO
                tokens = type_contract.functions.numberOfTokens().call()
                print("NUMBER OF TOKENS", tokens)
            else:
                tokens = 0
            
    return matching_contracts, types, total_blocks

def get_all_token_hashes(check_type, total_blocks):
    return [w3.eth.get_block(n)["transactions"][0].hex()
            for n in range(1, total_blocks+1)
            if w3.eth.get_transaction(w3.eth.get_block(n)["transactions"][0].hex())["to"] in check_type]
    
def get_nfts(contracts, check_type, total_blocks):
    
    all_token_hashs = get_all_token_hashes(check_type, total_blocks)
    
    print(w3.eth.getTransaction(all_token_hashs[0]))
    
    history_array = []
    index = 0
    for token in all_token_hashs:
        transaction = w3.eth.getTransaction(token)
        
        print("\nTRANSACTION", transaction)
        

        history = contracts[index].decode_function_input(transaction.input)
        history_array.append(history)
        print("\n\nHISTORY", history)
        index + 1
    return history_array

def check_bytecode_type(type, bc, known_bytecode):
    print("\nHERE\n")
    print("\n\n\nBYTECODE", bc[:-64])
    #print("\n\n\nKNONW BC", known_bytecode)
    
    print("\n", bc == "0x" + known_bytecode)

    if type == "machine" and bc == "0x" + known_bytecode:
        return type
    elif type == "data" and bc[:-64] == "0x" + known_bytecode:
        return type
    elif type == "prescription" and bc[:-64] == "0x" + known_bytecode:
        return type
    else:
        return ""