from web3 import Web3
from urllib.request import urlopen
from datetime import datetime

import contractDetailsMachineToken as mta  # machine token abi
import contractDetailsPatientToken as pta  # patient token abi
import contractDetailsPrescriptionToken as preta  # prescription token abi
import contractDetailsDataToken as dta  # data token abi


class txnDetails:
    def __init__(
        self, txn_hash: str,
        blkNum: int,
        _from: str,
        _to: str,
        e_from: str,
        e_to: str,
        gasPrice: float,
        eventLog: str,
        age_short: str,
        age_long: str,
    ):
        self.txn_hash = txn_hash
        self.blkNum = blkNum
        self._from = _from
        self._to = _to
        self.e_from = e_from
        self.e_to = e_to
        self.gasPrice = gasPrice
        self.eventLog = eventLog
        self.age_short = age_short
        self.age_long = age_long
        
        
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


async def getTransactionDetails(w3, cType, txn_hash):

    details = []

    txn = w3.eth.get_transaction(txn_hash)

    ca = txn["to"]
    print(ca)

    _from = txn["from"]
    print(_from)

    blk = txn["blockNumber"]
    print(blk)
    
    tx_timestamp = datetime.fromtimestamp(w3.eth.get_block(blk).timestamp)
        
    age = await cal_timediff(tx_timestamp)

    gasPrice = txn["gasPrice"] if txn["gasPrice"] is not None else 0
    gasPrice = float(w3.fromWei(gasPrice, 'ether'))

    matchContract = {
        'mta': w3.eth.contract(address=ca, abi=mta.abi),
        'pta': w3.eth.contract(address=ca, abi=pta.abi),
        'preta': w3.eth.contract(address=ca, abi=preta.abi),
        'dta':  w3.eth.contract(address=ca, abi=dta.abi)
    }

    contract = matchContract[cType]

    history = contract.decode_function_input(txn.input)
    print(history)

    eventLog = str(history[0])
    print("EVENTTTTTTTTTTTTTT ", eventLog)

    from_Event_address = {
        '<Function mint(string)>': "NullAddress",
        '<Function transferTokenOwnership(address,uint256)>': _from,
        '<Function addNewPatient(address,address,address)>': 'NullAddress',
        '<Function mintPrescriptionToken(string,uint256)>': 'NullAddress',
        "<Function mintDataToken(string,uint256,uint256)>": 'NullAddress',
    }

    e_from = from_Event_address[eventLog]

    to_Event_address = {
        '<Function mint(string)>': _from,
        '<Function transferTokenOwnership(address,uint256)>': history[1]['_to'] if e_from != "NullAddress" else "",
        '<Function addNewPatient(address,address,address)>': _from,
        '<Function mintPrescriptionToken(string,uint256)>': _from,
        "<Function mintDataToken(string,uint256,uint256)>": _from,
    }

    e_to = to_Event_address[eventLog]

    details = txnDetails(
        txn_hash,
        blk,
        _from,
        ca,
        e_from,
        e_to,
        gasPrice,
        eventLog,
        age,
        str(tx_timestamp)
    )

    return details
