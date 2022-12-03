from deployMachine import w3
import deployMachine
import json


def transfer_machine_ownership_to_doctor(doctor_address):
    # this should be manufacturer's address
    w3.eth.default_account = w3.eth.accounts[4]

    machine_contract = deployMachine.contract_deployed
    token_id = deployMachine.token_id

    machine_contract.functions.transferTokenOwnership(
        doctor_address, token_id).transact()
    event = machine_contract.events.TokenOwnershipTransfered().getLogs()
    print("TOKEN OWNERSHIP TRANSFER EVENT", event)
    token_id = event[0]["args"]["tokenId"]
    new_owner = machine_contract.functions.getTokenOwner(token_id).call()
    print("NEW OWNER", new_owner)
    if (new_owner == doctor_address):
        print("TRANSFER SUCCESSFUL")
    else:
        print("TRANSFER FAILED")


def transfer_machine_ownership_to_patient(input_info):

    token_id = json.loads(input_info)['machineTokenId']
    doctor_address_str = json.loads(input_info)['doctor']
    doctor_address = doctor_address_str.strip()
    patient_address_str = json.loads(input_info)['patient']
    patient_address = patient_address_str.strip()

    w3.eth.default_account = doctor_address

    machine_contract = deployMachine.contract_deployed

    machine_contract.functions.transferTokenOwnership(
        str(patient_address), int(token_id)).transact()
    event = machine_contract.events.TokenOwnershipTransfered().getLogs()
    print("TOKEN OWNERSHIP TRANSFER EVENT", event)
    new_owner = machine_contract.functions.getTokenOwner(int(token_id)).call()
    print("NEW OWNER", new_owner)
    if (new_owner == patient_address):
        print("TRANSFER SUCCESSFUL")
    else:
        print("TRANSFER FAILED")
