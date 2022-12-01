import IPFSv2
import dataTokenABI
import patientTokenABI
import prescriptionTokenABI
import json

from deployMachine import w3

doctor_patient_dict = {}


def register_new_patient(input_info):
    patient_address = json.loads(input_info)['patient']
    doctor_address = json.loads(input_info)['doctor']

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


def check_for_patient_contract(doctor_address):
    global doctor_patient_dict
    global patient_contract

    if (len(doctor_patient_dict) == 0):
        patient_contract = deploy_patient_contract(doctor_address)
    elif (not doctor_address in doctor_patient_dict):
        patient_contract = deploy_patient_contract(doctor_address)
    elif (doctor_address in doctor_patient_dict):
        patient_contract = doctor_patient_dict[doctor_address]
    return patient_contract


def check_for_patient_data(doctor_address, patient_address):
    global patient_contract
    global prescription_contract
    global data_contract

    w3.eth.default_account = doctor_address
    if (patient_contract.functions.checkIfPatientExists(patient_address).call()):
        data_contract_address, prescription_contract_address = patient_contract.functions.getPatient(
            patient_address).call()
        prescription_contract = w3.eth.contract(
            address=prescription_contract_address, abi=prescriptionTokenABI.abi
        )
        data_contract = w3.eth.contract(
            address=data_contract_address, abi=dataTokenABI.abi
        )
        w3.eth.default_account = doctor_address
        print("PATIENT", patient_address)
        print("DOCTOR", doctor_address)
        print("PRESCRIPTION CONTRACT ADDRESS", prescription_contract_address)
        print("DATA CONTRACT ADDRESS", data_contract_address)
    else:
        prescription_contract = deploy_prescription_contract(
            doctor_address, patient_address)
        data_contract = deploy_data_contract(patient_address, doctor_address)
        w3.eth.default_account = doctor_address
        patient_contract.functions.addNewPatient(
            patient_address, data_contract.address, prescription_contract.address).transact()
        print("PATIENT", patient_address)
        print("DOCTOR", doctor_address)
        print("PRESCRIPTION CONTRACT ADDRESS", prescription_contract.address)
        print("DATA CONTRACT ADDRESS", data_contract.address)
    return prescription_contract, data_contract


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
    print("PATIENT CONTRACT ADDRESS: ", patient_contract_address)
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
    print("PRESCRIPTION CONTRACT ADDRESS: ", prescription_contract_address)
    # deploy data contract (creates an instance of a contract) with the address above
    prescription_contract_deployed = w3.eth.contract(
        address=prescription_contract_address, abi=prescriptionTokenABI.abi
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
    print("DATA CONTRACT ADDRESS: ", data_contract_address)
    # deploy data contract (creates an instance of a contract) with the address above
    data_contract_deployed = w3.eth.contract(
        address=data_contract_address, abi=dataTokenABI.abi
    )
    return data_contract_deployed
