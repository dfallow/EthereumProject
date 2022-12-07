from web3 import Web3
from urllib.request import urlopen
from datetime import datetime

import contractDetailsMachineToken as mta  # machine token abi
import contractDetailsPatientToken as pta  # patient token abi
import contractDetailsPrescriptionToken as preta  # prescription token abi
import contractDetailsDataToken as dta  # data token abi

def getSingleTokenActivity(w3, ca, tid):
    return 0