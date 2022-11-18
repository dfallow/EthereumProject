import newDeployNFT

def sendNFT(_from, _to, _tokenId):
    print("---1---")
    mint_txn = newDeployNFT.contract_deployed.functions.transferFrom(_from.address, _to.address, _tokenId).build_transaction(
    {
        'from': _from.address,
        'nonce': 1,
        'gas': 1000000,
        'gasPrice': newDeployNFT.w3.toWei("70", "gwei"),

    }
    )
    print("---2---")

    signed_txn = newDeployNFT.w3.eth.account.sign_transaction(mint_txn, 
    private_key=_from.key)
    print("---3---")
    # It breakes here for some reason
    newDeployNFT.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print("---4---")
    
    #newDeployNFT.contract_deployed.functions.changeOwnerOfToken(_to, _tokenId).transact()

