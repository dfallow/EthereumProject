import IPFSv2
import dataTokenABI
import patientTokenABI
import prescriptionTokenABI
from web3 import Web3
import json

from newDeployNFT import w3

doctor_patient_dict = {}


def deploy_nfts(input_info):

    global patient_contract
    global data_contract

    files_object = json.loads(input_info)['metaData']
    machine_id = json.loads(input_info)['machineId']
    prescription_id = json.loads(input_info)['prescriptionId']
    doctor_address = json.loads(input_info)['doctorAddress']
    patient_address = json.loads(input_info)['patientAddress']

    # returns two arrays which show the location in IPFS of each file
    hash_array, url_array = create_files_to_store(
        files_object['name'], files_object['image'])

    # check if patient (registry) contract for the doctor is deployed already
    # it should only be deployed once per doctor
    # it keeps a registry of doctor's patients
    # if contract doesn't exists, then a new one is deployed
    print("Check for patient contract")
    check_for_patient_contract(doctor_address)

    # check if this particular patient is already in the registry
    # if not, new patient data contract and prescription contract is deployed and the patient is added to the registry (patient_contract)
    # data contract and prescription contract are deployed once per doctor's patient atm
    print("Check for patient data")
    check_for_patient_data(doctor_address, patient_address)

    # deploy nfts
    # the patient is the one who mints data nfts and who owns them
    w3.eth.default_account = patient_address
    print("Start deploying NFTs")
    for url in url_array:
        data_contract
        data_contract.functions.mintDataToken(
            url, int(machine_id), int(prescription_id)).transact()
        mintEvent = data_contract.events.Minted().getLogs()
        print("MINTED EVENT", mintEvent)
        tokenId = mintEvent[0]["args"]["nftId"]
        print("NFT ID/TokenId", tokenId)
        dataSaved = data_contract.functions.getDataItemForToken(tokenId).call()
        item_machine_id = dataSaved[1]
        item_prescription_id = dataSaved[2]
        item_url = dataSaved[3]
        print("DATA ITEM FOR TOKEN {} SAVED: MachineID {}, prescriptionID {}, IPFS url: {}". format(
            tokenId, item_machine_id, item_prescription_id, item_url))
    print("End of NFT deployment")
    print("BLOCK number", w3.eth.block_number)

    return


def create_files_to_store(name, files):
    files_array = files.split(",")

    files_hash_array = []
    files_url_array = []

    for file in files_array:
        # Store single file in ipfs
        file_hash, file_url = IPFSv2.store_ipfs_file_only_hash(
            name, file, files_array.index(file))
        # Store single file in ipfs
        # file_hash, file_url = IPFSv2.store_ipfs_file_only_hash(name, file[1:-1], files_array.index(file))
        files_hash_array.append(file_hash)
        files_url_array.append(file_url)
    return files_hash_array, files_url_array


def check_for_patient_contract(doctor_address):
    global doctor_patient_dict
    global patient_contract

    if (len(doctor_patient_dict) == 0):
        patient_contract = deploy_patient_contract(doctor_address)
    elif (not doctor_address in doctor_patient_dict):
        patient_contract = deploy_patient_contract(doctor_address)
    elif (doctor_address in doctor_patient_dict):
        patient_contract = doctor_patient_dict[doctor_address]
    return


def check_for_patient_data(doctor_address, patient_address):
    global patient_contract
    global prescription_contract
    global data_contract

    w3.eth.default_account = doctor_address
    if (patient_contract.functions.checkIfPatientExists(patient_address).call()):
        # atm prescription contract isn't deployed so the address is set to be the same as data contract
        # TODO: deploy prescription contract
        data_contract_address, prescription_contract_address = patient_contract.functions.getPatient(
            patient_address).call()
        prescription_contract = w3.eth.contract(
            address=prescription_contract_address, abi=prescriptionTokenABI.abi
        )
        data_contract = w3.eth.contract(
            address=data_contract_address, abi=dataTokenABI.abi
        )
        w3.eth.default_account = doctor_address
    else:
        prescription_contract = deploy_prescription_contract(
            doctor_address, patient_address)
        data_contract = deploy_data_contract(patient_address, doctor_address)
        w3.eth.default_account = doctor_address
        patient_contract.functions.addNewPatient(
            patient_address, data_contract.address, prescription_contract.address).transact()
    return


def deploy_patient_contract(doctor_address):
    # deploy patient contract
    # this should be done once per doctor
    w3.eth.default_account = doctor_address
    patient_contract_compiled = w3.eth.contract(
        abi=patientTokenABI.abi, bytecode=patientTokenABI.bytecode)
    patient_contract_transaction_hash = patient_contract_compiled.constructor().transact()
    print("NEW PATIENT CONTRACT TRANSACTION HASH",
          patient_contract_transaction_hash)
    patient_contract_transaction_receipt = w3.eth.wait_for_transaction_receipt(
        patient_contract_transaction_hash)
    print("NEW PATIENT CONTRACT TRANSACTION RECEIPT",
          patient_contract_transaction_receipt)
    # retrieve data contract address
    patient_contract_address = patient_contract_transaction_receipt["contractAddress"]
    # deploy data contract (creates an instance of a contract) with the address above
    patient_contract_deployed = w3.eth.contract(
        address=patient_contract_address, abi=patientTokenABI.abi
    )
    global doctor_patient_dict
    doctor_patient_dict[doctor_address] = patient_contract_deployed
    print("New item added to doctorPatientDict", doctor_patient_dict)
    return patient_contract_deployed


def deploy_prescription_contract(doctor_address, patient_address):
    w3.eth.default_account = doctor_address
    prescription_contract_compiled = w3.eth.contract(
        abi=prescriptionTokenABI.abi, bytecode=prescriptionTokenABI.bytecode)
    prescription_contract_transaction_hash = prescription_contract_compiled.constructor(
        patient_address).transact()
    print("NEW PRESCRIPTION CONTRACT TRANSACTION HASH",
          prescription_contract_transaction_hash)
    prescription_contract_transaction_receipt = w3.eth.wait_for_transaction_receipt(
        prescription_contract_transaction_hash)
    print("NEW PRESCRIPTION CONTRACT TRANSACTION RECEIPT",
          prescription_contract_transaction_receipt)
    # retrieve data contract address
    prescription_contract_address = prescription_contract_transaction_receipt[
        "contractAddress"]
    # deploy data contract (creates an instance of a contract) with the address above
    prescription_contract_deployed = w3.eth.contract(
        address=prescription_contract_address, abi=patientTokenABI.abi
    )
    return prescription_contract_deployed


def deploy_data_contract(patient_address, doctor_address):
    w3.eth.default_account = patient_address
    # compile data contract
    data_contract_compiled = w3.eth.contract(
        abi=dataTokenABI.abi, bytecode=dataTokenABI.bytecode
    )
    data_contract_transaction_hash = data_contract_compiled.constructor(
        doctor_address).transact()
    print("NEW DATA CONTRACT TRANSACTION HASH", data_contract_transaction_hash)
    data_contract_transaction_receipt = w3.eth.wait_for_transaction_receipt(
        data_contract_transaction_hash)
    print("NEW DATA CONTRACT TRANSACTION RECEIPT",
          data_contract_transaction_receipt)
    # retrieve data contract address
    data_contract_address = data_contract_transaction_receipt["contractAddress"]
    # deploy data contract (creates an instance of a contract) with the address above
    data_contract_deployed = w3.eth.contract(
        address=data_contract_address, abi=dataTokenABI.abi
    )
    return data_contract_deployed


# def deploy_nfts_from_python(hashArray):
   # hash_array, url_array = create_files_to_store("Test", hashArray[1:-1])
   # return hash_array, url_array
