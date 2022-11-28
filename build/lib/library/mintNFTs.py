

def mint_nft(deployed_contract, file_hash):

    file_url = "https://ipfs.io/ipfs/" + file_hash


    deployed_contract.functions.saveData(file_hash, file_url).transact()

    deployed_contract.functions.mint(file_url).transact()

    event = deployed_contract.events.Minted().getLogs()
    print("MINTED EVENT", event)
    tokenId = event[0]["args"]["nftId"]
    print("NFT ID/TokenId", tokenId)

    return

