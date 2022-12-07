from web3 import Web3
from urllib.request import urlopen
from datetime import datetime

import contractDetailsMachineToken as mta  # machine token abi
import contractDetailsPatientToken as pta  # patient token abi
import contractDetailsPrescriptionToken as preta  # prescription token abi
import contractDetailsDataToken as dta  # data token abi

class tokenActivity:
    def __init__(
        self,event: str,
        _from: str,
        _to: str,
        age: str,
    ):
        self.event = event
        self._from = _from
        self._to = _to
        self.age = age
        
        
async def cal_timediff(tx_timestamp):
    
    current_timestamp = datetime.fromtimestamp(datetime.timestamp(datetime.now()))
    time_diff = current_timestamp - tx_timestamp
            
    # days
    if time_diff.days > 0:
        if time_diff.days > 1:
            age = str(time_diff.days) + " days"
        else:
            age = str(time_diff.days) + " day"
    # hours
    elif time_diff.seconds/(60*60) >= 1:
        if time_diff.seconds/(60*60) > 1:
            age = str(int(time_diff.seconds/(60*60))) + " hours"
        else:
            age = str(int(time_diff.seconds/(60*60))) + " hour"
    # minutes
    elif time_diff.seconds/60 >= 1 and time_diff.seconds/60 <= 59:
        if time_diff.seconds/60 > 1:
            age = str(int(time_diff.seconds/60)) + " minutes"
        else:
            age = str(int(time_diff.seconds/60)) + " minute" 
    # seconds
    else:
        age = str(time_diff.seconds) + " seconds"
    
    return age
    
        
async def getSingleTokenActivity(w3, ca, tid, c_type):
    
    # initalise a list to return it to html
    activity_data = []
    
    # get to know total number of blocks on the chain
    numOfBLK = w3.eth.block_number
    
    # provide access to the correct smart contract
    
    matchContract = {
        'machine': w3.eth.contract(address=ca, abi=mta.abi),
        'prescription': w3.eth.contract(address=ca, abi=preta.abi),
        'data':  w3.eth.contract(address=ca, abi=dta.abi)
    }
    contract = matchContract[c_type]
    
    # firstly get the minted activity
    minted = contract.events.Minted().createFilter(fromBlock="0x0").get_all_entries()[int(tid)-1]
    
    tx_timestamp = datetime.fromtimestamp(w3.eth.get_block(minted['blockNumber']).timestamp)
        
    age = await cal_timediff(tx_timestamp)

    activity_data.append(tokenActivity(
        minted["event"],
        "NullAddress",
        minted["args"]["minter"],
        age
    ))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return activity_data