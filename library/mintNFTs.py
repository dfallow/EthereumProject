

def mint_nft(deployed_contract, file_hash):

    file_url = "https://ipfs.io/ipfs/" + file_hash


    #deployed_contract.functions.saveData(file_hash, #file_url).transact()

    deployed_contract.functions.mint(file_url).transact()

    event = deployed_contract.events.Minted().getLogs()
    print("MINTED EVENT", event)
    tokenId = event[0]["args"]["tokenId"]
    print("NFT ID/TokenId", tokenId)

    #token_uri = deployed_contract.functions.tokenIdToURI(tokenId).call()

    #token_owner = deployed_contract.functions.tokenIdToOwner(tokenId).call()
    print("FILE", file_url)
    print("TOKEN", tokenId)
    return tokenId

def mint_data_nft(
    deployed_contract, 
    file_hash, 
    patient_account, 
    machine_token_id,
    precription_token_id
    ):
    
    file_url = "https://ipfs.io/ipfs/" + file_hash

    data_token_id = deployed_contract.functions.mintDataToken(
    file_url,
    machine_token_id,
    precription_token_id
    ).transact()

    print("mintNFTs", data_token_id)
    return data_token_id
