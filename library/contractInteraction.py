
# used when minting machine NFTs
def mint_machine_nft(deployed_contract, file_hash):

    file_url = "https://ipfs.io/ipfs/" + file_hash

    deployed_contract.functions.mint(file_url).transact()

    event = deployed_contract.events.Minted().getLogs()
    print("\nMINTED EVENT", event)
    tokenId = event[0]["args"]["tokenId"]
    print("\nNFT ID/TokenId", tokenId)

    return tokenId

# used when minting prescription NFTs
def mint_prescription_nft(
    deployed_contract, 
    file_hash
    ):

    file_url = "https://ipfs.io/ipfs/" + file_hash

    deployed_contract.functions.mintPrescriptionToken(file_url).transact()

    event = deployed_contract.events.Minted().getLogs()
    print("MINTED EVENT", event)
    tokenId = event[0]["args"]["nftId"]
    print("NFT ID/TokenId", tokenId)

    print("FILE", file_url)
    print("TOKEN", tokenId)
    return tokenId

# use when minting the data files produces by the machine
def mint_data_nft(
    deployed_contract, 
    file_hash,  
    machine_token_id,
    precription_token_id
    ):
    
    file_url = "https://ipfs.io/ipfs/" + file_hash

    data_token_id = deployed_contract.functions.mintDataToken(
    file_url,
    machine_token_id,
    precription_token_id
    ).transact()

    mint_event = deployed_contract.events.Minted().getLogs()
    print("\nMINTED EVENT", mint_event)
    tokenId = mint_event[0]["args"]["nftId"]
    print("\nNFT ID/TokenId", tokenId)

    return tokenId


def add_new_patient(
    deployed_contract, 
    patient, 
    data_contract, 
    prescription_contract
    ):

    patient_exists = deployed_contract.functions.checkIfPatientExists(patient).call()

    print("PATIENT EXISTS", patient_exists)

    if patient_exists:
        print("Patient Already Is Registered")
        return patient_exists, "", "", ""
    else:
        deployed_contract.functions.addNewPatient(
            patient,
            data_contract,
            prescription_contract
        ).transact()
        print("Patient Added") 
        return  patient_exists, patient, data_contract, prescription_contract


def transfer_contract_ownership(contract, target_account):
    
    contract.functions.transferOwnership(target_account).transact()
    
    tranfer_contract_event = contract.events.ContractOwnershipTransfered().getLogs()
    
    print("\nTransfer Ownership Event", transfer_contract_ownership)
    
    return

def transfer_token_ownership(contract, target_account, token_id):
    
    contract.functions.transferTokenOwnership(target_account, token_id).transact()
    
    transfer_token_event = contract.events.TokenOwnershipTransfered().getLogs()
    print("\nTransfer Token Event", transfer_token_event)
    
    test = transfer_token_event[0]['args']
    

    print("\nNFT ID/TokenId", test)
    
    return

def transfer_ownership_multiple_tokens(
    contract, 
    target_account, 
    tokens
    ):
    
    contract.functions.transferTokenOwnership(
        target_account,
        tokens
    ).transact()
    
    transfer_tokens_event = contract.events.TokenOwnershipTransfered().getLogs()
    
    print("TRANSFER EVENT", transfer_tokens_event)
    
    
    return

