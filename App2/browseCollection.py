from web3 import Web3
import json
import os
import sys
from urllib.request import urlopen
from urllib.error import HTTPError
import json

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

async def getSmartContractCreator(w3, target_ca):
    numOfBLK = w3.eth.block_number
    # dig deep into the history of each block
    # and check which address(user) minted the smart contract
    for i in range(1, numOfBLK+1):
        check_mint_txh = w3.eth.get_block(i)["transactions"][0].hex()
        mint_receipt =  w3.eth.get_transaction_receipt(check_mint_txh)
        if mint_receipt["logs"][0]["address"] == target_ca:
            return mint_receipt["from"]
        
     
async def getUrlResponse(url):

    try:
        req = urlopen(url)
    except HTTPError:
        return None
    
    if int(req.status) != 504 or int(req.status) != 429:
        print("request status", req.status)
        md_json = json.loads(req.read())
        req.close()
        return md_json
    else: return None   

async def getMetaData(md_url):
    print("now get response to: ", md_url)
    res = await getUrlResponse(md_url)
    
    return res
     
async def recur(w3, target_ca, tokens, res=None):
    
    print("wait for sending requests to", tokens)
    
    if res == None:
        res = []
    
    if tokens == []:
        return res

    # pop out token id
    contract = w3.eth.contract(address=target_ca, abi=cd.abi)
    num = tokens.pop()
    cur_token = tokens
    
    
    # get one metadata ipfs url
    md_url = contract.functions.dataItems(num).call()[-1]
    md = await getMetaData(md_url)
    print("GET METADATA: ", md)
    
    # get metadata from url response
    res.append(NFTs(target_ca,
                    md_url,
                    md["image"] if md else "https://ipfs.io/ipfs/Qmdgud3qvpxqbTYkk4x71FUV4zvfUufu377GQeprqokof4",
                    md["name"] if md else "try later",
                    md["attributes"][0]["department"] if md else "try later",
                    num + 1,
                    contract.functions.getOwnerOfToken(num+1).call()))
    
    await recur(w3, target_ca, cur_token, res)
    
    return res

async def getNFTsBySmartContract(w3, target_ca):
    # initialise a object list
    NFTs_data = []
    
    # access to the smart contract
    contract = w3.eth.contract(address=target_ca, abi=cd.abi)
    # get the total number of token in this smart contract
    numOfNFTs = contract.functions.totalSupply().call()
    
    tokens = [x for x in range(numOfNFTs)]
    
    NFTs_data += await recur(w3, target_ca, tokens)
    
    return sorted(NFTs_data, key=lambda x: x.tokenId)
    
    
    
    

