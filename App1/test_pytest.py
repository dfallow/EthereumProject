from deployNFT import Web3
import deployNFT

def test_is_connected():
    assert deployNFT.is_connected(deployNFT.w3) == True


def test_default_account():
    deployNFT.w3.eth.default_account == deployNFT.w3.eth.accounts[0]
