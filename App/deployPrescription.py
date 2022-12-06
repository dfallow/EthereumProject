import IPFS
import json
import deployPatient
import connection
from deployMachine import w3
from deployMachine import contract_deployed as machine_contract

validated_successfully = False


def deploy_prescription_nft(info_object):
    global validated_successfully

    patient_address = json.loads(info_object)['patient']
    doctor_address = json.loads(info_object)['doctor']
    file_name = json.loads(info_object)['image']
    machine_token_id = json.loads(info_object)['machineTokenId']

    w3.eth.default_account = doctor_address
    validate_doctor_machine_owner(doctor_address, machine_token_id)

    if validated_successfully == False:
        return
    else:
        deployPatient.check_for_patient_contract(doctor_address)

        prescription_contract, data_contract = deployPatient.check_for_patient_data(
            doctor_address, patient_address)

        # store metadata file on IPFS
        file_hash, file_url = IPFS.store_ipfs_file(file_name, info_object)
        # mint prescription NFT
        prescription_contract.functions.mintPrescriptionToken(
            file_url, int(machine_token_id)).transact()
        event = prescription_contract.events.Minted().getLogs()
        print("MINTED EVENT", event)
        tokenId = event[0]["args"]["tokenId"]
        print("PRESCRIPTION TOKEN ID", tokenId)
        # get NFT count
        print("Prescription count",
              prescription_contract.functions.numberOfPrescriptionTokens().call())
        print("BLOCK number", w3.eth.block_number)


def validate_doctor_machine_owner(doctor_address, machine_token_id):
    global validated_successfully
    token_owner = machine_contract.functions.getTokenOwner(
        int(machine_token_id)).call()
    if token_owner != doctor_address:
        print("CANNOT PERFORM THE ACTION: DOCTOR IS NOT THE CURRENT OWNER OF MACHINE TOKEN")
        validated_successfully = False
        return
    else:
        validated_successfully = True
        return
