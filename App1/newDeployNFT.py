import IPFSv2
import newContractDetails
from web3 import Web3

# test environment
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
# w3 = Web3(Web3.EthereumTesterProvider())

w3.eth.default_account = w3.eth.accounts[1]

# check if connected successfully
print("IS CONNECTED", w3.isConnected())

# can run when needed to check connection
def is_connected(w3):
    return w3.isConnected()

# compile contract
contract_compiled = w3.eth.contract(
    abi=newContractDetails.abi, bytecode=newContractDetails.bytecode
)

transaction_hash = contract_compiled.constructor().transact()
print("TRANSACTION HASH", transaction_hash)
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
print("TRANSACTION RECEIPT", transaction_receipt)

# retrieve contract address
contract_address = transaction_receipt["contractAddress"]

# deploy contract (creates an instance of a contract) with the address above
contract_deployed = w3.eth.contract(
    address=contract_address, abi=newContractDetails.abi
)



def new_deploy_nft(file_name, info_object):

    # store file on IPFS and return it's hash and url
    # ipfs daemon has to be running in the terminal
    file_hash, file_url = IPFSv2.store_ipfs_file(file_name, info_object)

    # save data
    print("SAVE", contract_deployed.functions.saveData(
        file_hash, file_url).transact())
    # mint NFT
    print("MINTED", contract_deployed.functions.mint(file_url).transact())

    # Minted event log below shows tokenId, and url to metadata file and other things
    # as long as connection isn't restarted and you keep adding new pictures/creating new NFT,
    #  the tokenId number will keep on changing but the contract address should remain the same
    # so all NFTs will be located under the same contract address
    # on OpenSea for example, our NFT url would basically the same as contract url but it ends w
    # ith /tokenId for example, https://someurl.com/contractAddressHash/tokenId
    event = contract_deployed.events.Minted().getLogs()
    print("MINTED EVENT", event)
    tokenId = event[0]["args"]["nftId"]
    print("NFT ID/TokenId", tokenId)

    # get totalSupply(NFT count)
    print("NFT count", contract_deployed.functions.totalSupply().call())

    # get URI of token
    print("URI", contract_deployed.functions.tokenIdToURI(tokenId).call())

    #to get owner of NFT can use either tokenIdToOwner mapping or function getOwnerOfToken(tokenId)
    # this uses mapping
    print("OWNER", contract_deployed.functions.tokenIdToOwner(tokenId).call())

    print("BLOCK number", w3.eth.block_number)
