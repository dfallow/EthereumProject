from web3 import Web3
import json
import time
from urllib.request import urlopen
from urllib.error import URLError
import os
import sys
# import requests_async as requests

sys.path.append(os.path.abspath(os.path.join('.')))
from App1 import newContractDetails as cd
class NFTs:
    def __init__(
        self, contractAddress: str,
        ipfs_metadata: str,
        img_ipfs: str,
        name: str,
        collection: str,
        tokenId: int,
        owner: str,
    ):
        self.contractAddress = contractAddress
        self.ipfs_metadata = ipfs_metadata
        self.img_ipfs = img_ipfs
        self.name = name,
        self.collection = collection
        self.tokenId = tokenId
        self.owner = owner
        
async def getUrlResponse(url):
    # time.sleep(3)
    req = urlopen(url)
    # req = requests.get(url, headers = {'User-agent': 'Super Bot Power Level Over 9000'})
    
    if int(req.status) != 504 or int(req.status) != 429:
        print("request status", req.status)
        md_json = json.loads(req.read())
        req.close()
        return md_json
    else:
        return None
    
async def getMetaData(url):
    # time.sleep(5)
    print("now get response to: ", url)
    res = await getUrlResponse(url)
    return res

# return all blocks with a valid smart contract
def getAllValidContractAddress(w3, nob):
    return list(set([
        w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"]
        for i in reversed(range(1, nob+1)) 
        if w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"] is not None 
    ]))
    
async def recur(w3, ca, tokens, res=None):
    
    print("TOKEN ID and CONTRACT ADDRESS", tokens, ca)
    
    if res == None:
        res = []
        
    if tokens == []:
        return res
    
    contract = w3.eth.contract(address=ca, abi=cd.abi)
    num = tokens.pop()
    cur_token = tokens
    print("TOKEEENNNN AGAIN", cur_token)
    md_ipfs = contract.functions.dataItems(num).call()[-1]
    
    print("md_ipfs", md_ipfs)
    
    # wait until getMetaData finished
    md = await getMetaData(md_ipfs)
    
    print("GET METADATA: ", md)
    
    res.append(NFTs(ca,
                    md_ipfs,
                    md["image"] if md else "https://ipfs.io/ipfs/Qmdgud3qvpxqbTYkk4x71FUV4zvfUufu377GQeprqokof4",
                    md["name"] if md else "try later",
                    md["attributes"][0]["department"] if md else "try later",
                    num + 1,
                    contract.functions.getOwnerOfToken(num+1).call()))
    
    # recursion 
    await recur(w3, ca, cur_token, res)
    
    return res    
    

# get the NFTs a user owns
async def getMyNFTs(w3):

    # get total number of blocks on the chain
    numOfBLK = w3.eth.block_number
    
    # get list of contact address
    valid_ca = getAllValidContractAddress(w3, numOfBLK)
    print("ALL CONTRACT ADDRESS", valid_ca)
    
    # initialise a list to be returned
    myNFTs_data = []
    
    # if there's not contract address on chain, then early return
    if valid_ca == []:
        return []
    
    for ca in valid_ca:
        
        # access to smart contract
        contract = w3.eth.contract(address=ca, abi=cd.abi)
        
        # get token id owned by current user from smart contract
        ownedToken = [
            x for x in range(contract.functions.totalSupply().call())
            if contract.functions.getOwnerOfToken(x+1).call() == w3.eth.default_account 
        ]
        
        # get metadata from url response
        if ownedToken:
            myNFTs_data += await recur(w3, ca, ownedToken)
                
    # return owned NFTs and send them to transact page for displaying them
    return sorted(myNFTs_data, key=lambda x: x.collection, reverse=True)
  