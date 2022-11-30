
# used when minting machine NFTs
def mint_machine_nft(deployed_contract, file_hash):

    file_url = "https://ipfs.io/ipfs/" + file_hash

    deployed_contract.functions.mint(file_url).transact()

    event = deployed_contract.events.Minted().getLogs()
    print("MINTED EVENT", event)
    tokenId = event[0]["args"]["tokenId"]
    print("NFT ID/TokenId", tokenId)

    print("FILE", file_url)
    print("TOKEN", tokenId)
    return tokenId

# used when minting prescription NFTs
def mint_prescription_nft(deployed_contract, file_hash):

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

    print("mintNFTs", data_token_id)
    return mint_event[0]["args"]["nftId"]
