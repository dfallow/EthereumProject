import IPFSv2
import json
import registerPatient

from deployMachine import w3


def deploy_prescription_nft(info_object):

    patient_address = json.loads(info_object)['patient']
    doctor_address = json.loads(info_object)['doctor']
    file_name = json.loads(info_object)['image']

    w3.eth.default_account = doctor_address

    registerPatient.check_for_patient_contract(doctor_address)
    prescription_contract, data_contract = registerPatient.check_for_patient_data(
        doctor_address, patient_address)

    # store metadata file on IPFS
    file_hash, file_url = IPFSv2.store_ipfs_file(file_name, info_object)

    # mint prescription NFT
    prescription_contract.functions.mintPrescriptionToken(
        file_url).transact()

    event = prescription_contract.events.Minted().getLogs()
    print("MINTED EVENT", event)
    tokenId = event[0]["args"]["tokenId"]
    print("PRESCRIPTION TOKEN ID", tokenId)

    # get NFT count
    print("Prescription count",
          prescription_contract.functions.numberOfPrescriptionTokens().call())

    print("BLOCK number", w3.eth.block_number)
