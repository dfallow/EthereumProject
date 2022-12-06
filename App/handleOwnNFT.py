import json
from urllib.request import urlopen
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import contractDetailsMachineToken as mta  # machine token abi
import contractDetailsPatientToken as pta  # patient token abi
import contractDetailsPrescriptionToken as preta  # prescription token abi
import contractDetailsDataToken as dta  # data token abi


class Machine:
    def __init__(
        self, ca: str,  # contract address
        file_ipfs: str,  # assume it's just an image, it shd be sth like certificate for machine
        tid: int,  # token id
        owner: str,  # current owner
        c_owner: str,  # contract owner (manufacture)
    ):
        self.ca = ca
        self.file_ipfs = file_ipfs
        self.tid = tid
        self.owner = owner
        self.c_owner = c_owner


class Patient:
    def __init__(
        self, pca: str,  # patient contract address
        patientAddress: str,  # patient address
        dca: str,  # data contract address
        preca: str,  # prescription contract address
        icon: str,
    ):
        self.pca = pca
        self.patientAddress = patientAddress
        self.dca = dca
        self.preca = preca
        self.icon = icon


class Prescription:
    def __init__(
        self, preca: str,  # prescription contract address
        precaId: int,
        # machineId: str, # do this in detail
        # patient: str,
        # doctor: str,
        file_ipfs: str,
        owner: str,
        icon: str,
    ):
        self.preca = preca
        self.precaId = precaId
        # self.machineId = machineId
        # self.patient = patient
        # self.doctor = doctor
        self.file_ipfs = file_ipfs
        self.owner = owner
        self.icon = icon


class machineData:
    def __init__(
        self, dca: str,
        file_ipfs: str,
        owner: str,
        dataId: int,
        icon: str,
    ):
        self.dca = dca
        self.file_ipfs = file_ipfs
        self.owner = owner
        self.dataId = dataId
        self.icon = icon


async def ownMachine(w3, machineContractAddress):

    if machineContractAddress == []:
        return []

    res = []

    # look through all contracts and see does the current users own some token
    for mca in machineContractAddress:

        # access the smart contract
        contract = w3.eth.contract(address=mca, abi=mta.abi)

        # get the nunber of token current user owns in current smart contract
        ownedTokens = [
            x+1 for x in range(contract.functions.totalMachineTokens().call())
            if contract.functions.getTokenOwner(x+1).call() == w3.eth.default_account
        ]

        for token in ownedTokens:
            res.append(Machine(
                mca,
                "https://ipfs.io/ipfs/QmTLptGFCZymukEJkjLwoZZfyXS34CYE4dffscW9ZZbm1j",
                token,
                w3.eth.default_account,
                contract.functions.owner().call()
            ))

    return res


async def ownPatient(w3, patientContractAddress):

    if patientContractAddress == []:
        return []

    res = []

    for pca in patientContractAddress:

        # access to the patient smart contract
        contract = w3.eth.contract(address=pca, abi=pta.abi)

        if contract.functions.owner().call() == w3.eth.default_account:

            patientInfo = contract.functions.getAllPatients().call()

            # patientAddress, dataContract, prescriptionContract
            listOfPA = patientInfo[0]
            listOfDC = patientInfo[1]
            listOfPreC = patientInfo[2]

            numOfPatients = contract.functions.numberOfPatients().call()

            for nop in range(numOfPatients):
                res.append(Patient(
                    pca,
                    listOfPA[nop],
                    listOfDC[nop],
                    listOfPreC[nop],
                    "https://ipfs.io/ipfs/Qmbhc2oV2m31EaSegooRBX9iF2XcfKjJLh6dfUkwQXsdpP",
                ))
    return res


async def getUrlResponse(url):
    try:
        req = urlopen(url)
    except HTTPError:
        return None
    except URLError:
        return None

    if int(req.status) != 504 or int(req.status) != 429:
        print("request status", req.status)
        md_json = json.loads(req.read())
        req.close()
        return md_json
    else:
        return None


async def getMetaData(md_url):

    print("now get response to: ", md_url)
    res = await getUrlResponse(md_url)
    print(res)
    return res


async def ownPerscription(w3, prescriptionContractAddress):

    print("PRESCRIPTION ADDRESS", prescriptionContractAddress)

    if prescriptionContractAddress == []:
        return []

    res = []

    for preca in prescriptionContractAddress:

        # access to the prescription smart contract
        contract = w3.eth.contract(address=preca, abi=preta.abi)

        # number of prescription in this current smart contract
        numOfPre = contract.functions.numberOfPrescriptionTokens().call()

        # see if current user is the patient or doctor or not related(restricted)
        try:
            md_url = contract.functions.tokenURI(1).call()
            # print("I GOT THE url", md_url)
        except:
            pass
        else:
            for pre in range(numOfPre):
                md_url = contract.functions.tokenURI(pre+1).call()

                owner = contract.functions.owner().call()

                # prescriptionMetaData = await getMetaData(md_url)
                # print(prescriptionMetaData)

                # print("before, ", res)

                res.append(Prescription(
                    preca=preca,
                    precaId=pre+1,
                    file_ipfs=md_url,
                    owner=owner,
                    # machineId=prescriptionMetaData["machineTokenId"] if prescriptionMetaData is not None else "try later",
                    # patient=prescriptionMetaData["patient"]if prescriptionMetaData is not None else "try later",
                    # doctor=prescriptionMetaData["doctor"]if prescriptionMetaData is not None else "try later",
                    # file_ipfs=prescriptionMetaData["image"]if prescriptionMetaData is not None else "try later",
                    icon="https://ipfs.io/ipfs/QmWUGLPniCt7AXLS8B68MCTY4BBaE6cnMtwUeXwjX2azLY"
                ))

    return res


async def ownMachineData(w3, dataContractAddress):

    print("DATA CONTRACT ADDRESS: ", dataContractAddress)

    if dataContractAddress == []:
        return []

    res = []

    for dca in dataContractAddress:

        # access to the data smart contract
        contract = w3.eth.contract(address=dca, abi=dta.abi)

        # number of data token in this current smart contract
        numOfTokens = contract.functions._numberOfDataTokens().call()

        for token in range(numOfTokens):

            try:
                md_url = contract.functions.tokenURI(token+1).call()
            except:
                print("Third Party: permission denied")
                pass
            else:
                md_url = contract.functions.tokenURI(token+1).call()

                owner = contract.functions.owner().call()

                res.append(machineData(
                    dca,
                    md_url,
                    owner,
                    token+1,
                    icon="https://ipfs.io/ipfs/QmUxPgmvw99jekV1uLrCjEBQcTQg3VQb9bgg5T4QMdBgGC"
                ))

    return res


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
            ca = w3.eth.get_transaction_receipt(w3.eth.get_block(
                n)["transactions"][0].hex())["contractAddress"]

            # bytecode
            bc = w3.eth.getTransaction(w3.eth.get_block(
                n)["transactions"][0].hex())["input"]

            # get the type of the bytecode
            bc_type = await checkTypeOfBytecode(bc)

            # check if the contract address contrains some token, if not, we won't store it
            if bc_type != "" and await checkContractAddressValidation(w3, ca, bc_type) == True:
                hm[ca] = bc_type

    return hm


async def getOwnNFTs(w3):

    numOfBLK = w3.eth.block_number

    caToType = await contractAddressToTypeOfSmartContract(w3, numOfBLK)

    print(caToType)

    machineContractAddress = [ca for ca in dict(
        filter(lambda elem: elem[1] == "mta", caToType.items()))]
    patientContractAddress = [ca for ca in dict(
        filter(lambda elem: elem[1] == "pta", caToType.items()))]
    prescriptionContractAddress = [ca for ca in dict(
        filter(lambda elem: elem[1] == "preta", caToType.items()))]
    dataContractAddress = [ca for ca in dict(
        filter(lambda elem: elem[1] == "dta", caToType.items()))]

    machine = await ownMachine(w3, machineContractAddress)
    patient = await ownPatient(w3, patientContractAddress)
    prescription = await ownPerscription(w3, prescriptionContractAddress)
    data = await ownMachineData(w3, dataContractAddress)

    return machine, patient, prescription, data
