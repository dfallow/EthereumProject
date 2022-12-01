import IPFSv2
import registerPatient
import json

from newDeployNFT import w3

doctor_patient_dict = {}


def deploy_nfts(input_info):

    global patient_contract
    global data_contract
    
    print("INPUT INFO", input_info)
    files_object = json.loads(input_info)['metaData']
    machine_id = json.loads(input_info)['machineId']
    prescription_id = json.loads(input_info)['prescriptionId']
    doctor_address_str = json.loads(input_info)['doctorAddress']
    doctor_address = doctor_address_str.strip()
    patient_address_str = json.loads(input_info)['patientAddress']
    patient_address = patient_address_str.strip()
    
    # returns two arrays which show the location in IPFS of each file
    hash_array, url_array = create_files_to_store(
        files_object['name'], files_object['image'])

    # check if patient (registry) contract for the doctor is deployed already
    # it should only be deployed once per doctor
    # it keeps a registry of doctor's patients
    # if contract doesn't exists, then a new one is deployed
    print("Check for patient contract")
    patient_contract = registerPatient.check_for_patient_contract(doctor_address)

    # check if this particular patient is already in the registry
    # if not, new patient data contract and prescription contract is deployed and the patient is added to the registry (patient_contract)
    # data contract and prescription contract are deployed once per doctor's patient atm
    print("Check for patient data")
    prescription_contract, data_contract = registerPatient.check_for_patient_data(doctor_address, patient_address)

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


# def deploy_nfts_from_python(hashArray):
   # hash_array, url_array = create_files_to_store("Test", hashArray[1:-1])
   # return hash_array, url_array
