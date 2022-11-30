import IPFSv2
import dataTokenABI
import patientTokenABI
import prescriptionTokenABI
from web3 import Web3
import json

from newDeployNFT import w3

w3.eth.default_account = w3.eth.accounts[0]
# compile contract
contract_compiled = w3.eth.contract(
    abi=prescriptionTokenABI.abi, bytecode=prescriptionTokenABI.bytecode
)

transaction_hash = contract_compiled.constructor().transact()
print("PRESCRIPTION CONTRACT TRANSACTION HASH", transaction_hash)
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
print("PRESCRIPTION CONTRACT TRANSACTION RECEIPT", transaction_receipt)
contract_address = transaction_receipt["contractAddress"]
prescription_contract = w3.eth.contract(
    address=contract_address, abi=prescriptionTokenABI.abi
)


def deploy_prescription_nft(info_object):

    patient_address = json.loads(info_object)['patient']
    file_name = json.loads(info_object)['image']

    # store metadata file on IPFS
    file_hash, file_url = IPFSv2.store_ipfs_file(file_name, info_object)

    # mint prescription NFT
    prescription_contract.functions.mintPrescriptionToken(
        file_url, patient_address).transact()

    event = prescription_contract.events.Minted().getLogs()
    print("MINTED EVENT", event)
    tokenId = event[0]["args"]["tokenId"]
    print("TokenId", tokenId)

    # get NFT count
    print("Prescription count",
          prescription_contract.functions.numberOfPrescriptionTokens().call())

    print("GET PRESCRIPTION BY TOKEN ID",
          prescription_contract.functions.getPrescriptionByTokenId(tokenId).call())

    print("GET PRESCRIPTIONS BY PATIENT",
          prescription_contract.functions.getPrescriptionsByPatient(patient_address).call())

    print("BLOCK number", w3.eth.block_number)
