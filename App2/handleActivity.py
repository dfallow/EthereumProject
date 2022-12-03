from web3 import Web3
import json
import os
import sys
from urllib.request import urlopen

sys.path.append(os.path.abspath(os.path.join('.')))
from App1 import machineTokenABI as mta # machine token abi
from App1 import patientTokenABI as pta # patient token abi
from App1 import prescriptionTokenABI as preta # prescription token abi 
from App1 import dataTokenABI as dta # data token abi


# loop through the blocks

# get all valid ca which means "to" 

# check input (abi bytecode) to determine which contract

# then check event log to see what's the action


class allActivityData:
    def __init__(
        self, txn_hash: str,
        event: str,
        contract: str,
        blkNum: int,
        _from: str,
        _to: str,
    ):
        self.txn_hash = txn_hash
        self.event = event
        self.contract = contract
        self.blkNum = blkNum
        self._from = _from  
        self._to = _to
 
 
 
async def checkContractAddressValidation(w3, ca, bc_type):
    
    # print(ca, bc_type)
    
    matchContract = {
        'mta': w3.eth.contract(address=ca, abi=mta.abi),
        'pta': w3.eth.contract(address=ca, abi=pta.abi),
        'preta': w3.eth.contract(address=ca, abi=preta.abi),
        'dta':  w3.eth.contract(address=ca, abi=dta.abi)
    }
    
    contract = matchContract[bc_type]
    
    checkNumOfToken = {
        "mta": contract.functions.totalMachineTokens().call() if bc_type == "mta" else 0,
        "pta": contract.functions.numberOfPatients().call() if bc_type == "pta" else 0,
        "preta": contract.functions.numberOfPrescriptionTokens().call() if bc_type == "preta" else 0,
        "dta": contract.functions._numberOfDataTokens().call() if bc_type == "dta" else 0,
    }
    
    return True if checkNumOfToken[bc_type] > 0 else False 
 
async def checkTypeOfBytecode(bc):
    the_type = ""
    
    if bc == "0x" + mta.bytecode:
        the_type = "mta"
    elif bc == "0x" + pta.bytecode:
        the_type = "pta"
    elif bc[:(len(bc)-64)] == "0x" + preta.bytecode:
        the_type = "preta"
    elif bc[:(len(bc)-64)] == "0x" + dta.bytecode:
        the_type = "dta"

    return the_type
    
 
async def contractAddressToTypeOfSmartContract(w3, nob):
    hm = {}
    
    for n in range(1, nob+1):
        # to find the blocks in which a smart contract is created
        if (w3.eth.get_transaction(w3.eth.get_block(n)["transactions"][0].hex())["to"] == None and
        w3.eth.get_transaction_receipt(w3.eth.get_block(n)["transactions"][0].hex())["contractAddress"] not in hm):
            
            # contract address
            ca = w3.eth.get_transaction_receipt(w3.eth.get_block(n)["transactions"][0].hex())["contractAddress"]
            
            # bytecode
            bc = w3.eth.getTransaction(w3.eth.get_block(n)["transactions"][0].hex())["input"]

            # get the type of the bytecode
            bc_type = await checkTypeOfBytecode(bc)
            
            # check if the contract address contrains some token, if not, we won't store it
            if bc_type != "" and await checkContractAddressValidation(w3, ca, bc_type) == True:
                hm[ca] = bc_type  
            
    return hm


async def getAllValidTxh(w3, checkType, nob):
    return [w3.eth.get_block(n)["transactions"][0].hex()
            for n in range(1, nob+1)
            if w3.eth.get_transaction(w3.eth.get_block(n)["transactions"][0].hex())["to"] in checkType]

async def getInfo(w3, checkType, nob):
    
    data = []
    
    allValidTxh = await getAllValidTxh(w3, checkType, nob)
    
    for txh in allValidTxh:
        transaction = w3.eth.getTransaction(txh)
        ca = transaction["to"]
        # print("CONTRACT ADDRESS ", ca)
        cType = checkType[transaction["to"]]
        # print("THE TYPE OF CONTRACT ", cType)
        
        matchContract = {
            'mta': w3.eth.contract(address=ca, abi=mta.abi),
            'pta': w3.eth.contract(address=ca, abi=pta.abi),
            'preta': w3.eth.contract(address=ca, abi=preta.abi),
            'dta':  w3.eth.contract(address=ca, abi=dta.abi)
        }
        
        # matching the correct type of contract and its abi
        contract = matchContract[cType]
        
        history = contract.decode_function_input(transaction.input)
        
        # print(cType, str(history[0]), str(history[1]))
        
        event = ""
        _from = ""
        _to = ""
        
        
        mtaEvent = {
            '<Function mint(string)>': "Mint",
            '<Function transferTokenOwnership(address,uint256)>': 'transferTokenOwnership',
        }
        
        ptaEvent = {
            '<Function addNewPatient(address,address,address)>': 'addNewPatient'
        }
        
        pretaEvent = {
            '<Function mintPrescriptionToken(string)>': 'mintPrescriptionToken'
        }
        
        dtaEvent = {
            "<Function mintDataToken(string,uint256,uint256)>": 'mintDataToken',
        }
        
        if cType == "mta":
            event = mtaEvent[str(history[0])]
        elif cType == "pta":
            event = ptaEvent[str(history[0])]
        elif cType == "preta":
            event = pretaEvent[str(history[0])]
        elif cType == "dta":
            event = dtaEvent[str(history[0])]
            
        # print("REAL EVENT NAME ", event)
        
            
        txn_hash = transaction["hash"].hex()
        
        blk = transaction["blockNumber"]
        
        _fromAdd = {
            'Mint': "NullAddress",
            'addNewPatient': "NullAddress",
            'mintPrescriptionToken': "NullAddress",
            'mintDataToken': "NullAddress",
            'transferTokenOwnership': transaction["from"]
        }
        
        _toAdd = {
            'Mint': transaction["from"],
            'addNewPatient': transaction["from"],
            'mintPrescriptionToken': transaction["from"],
            'mintDataToken': transaction["from"],
            'transferTokenOwnership': history[1]['_to'] if event == "transferTokenOwnership" else ""
        }
        
        
        
        _from = _fromAdd[event]
        _to = _toAdd[event]
        
        # print("FROM AND TO", _from, _to)
        
        data.append(
            allActivityData(
                txn_hash,
                event,
                cType,
                blk,
                _from,
                _to
            )   
        )
        
    return data
        
        
            
    
async def getMedicalActivity(w3):
    
    # initialise a list to return it to html
    allMedicalActivity = []
    
    numOfBLK = w3.eth.block_number
    
    # get to know the type of the smart contract using by this contract address -> hash table
    caToType = await contractAddressToTypeOfSmartContract(w3, numOfBLK)
    
    # check all the blocks event with a valid contract address
    allMedicalActivity += await getInfo(w3, caToType, numOfBLK)
    
    return allMedicalActivity