from web3 import Web3
import json
from urllib.request import urlopen
import os
import sys
from urllib.request import urlopen
from urllib.error import URLError

sys.path.append(os.path.abspath(os.path.join('.')))
from App1 import machineTokenABI as mta # machine token abi
from App1 import patientTokenABI as pta # patient token abi
from App1 import prescriptionTokenABI as preta # prescription token abi 
from App1 import dataTokenABI as dta # data token abi

class NFTs:
    def __init__(
        self, ca: str,
        ipfs_metadata: str,
        file_ipfs: str,
        type: str,
        tid: int,
        owner: str,
        icon: str,
    ):
        self.ca = ca
        self.ipfs_metadata = ipfs_metadata
        self.file_ipfs = file_ipfs
        self.type = type
        self.tid = tid  
        self.owner = owner
        self.icon = icon

async def getOwnNFTs(w3):
    
    # initialise a list to be returned
    myNFTs_data = []


    # machine -> getTokenOwner -> getTokenURL
    
    
    
    return 0