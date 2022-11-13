import newDeployNFT

def test_is_connected():
    assert newDeployNFT.is_connected(newDeployNFT.w3) == True


#def test_default_account():
#    deployNFT.w3.eth.default_account == deployNFT.w3.eth.accounts[0]