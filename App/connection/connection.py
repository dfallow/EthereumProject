from flask import Flask, render_template, url_for, request, redirect
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))

import deployMachine
import deployMachineData
import deployPrescription
import deployPatient
import transferOwnership
from fetchBlockData import medicalActivity, txDetails, ownNFTs, ownNFTDetails, fakeLogin

from createGraphs import execute

## Returns /home/dfallow/Documents/EthereumProject
app_one_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
os.chdir(app_one_dir)

app = Flask(__name__)

app.add_url_rule('/login', methods=["GET", "POST"], view_func=fakeLogin)
app.add_url_rule('/medicalActivity', methods=["GET", "POST"], view_func=medicalActivity)
app.add_url_rule('/tx/<string:txn_hash>', methods=["GET", "POST"], view_func=txDetails)
app.add_url_rule('/ownnft', methods=["GET", "POST"], view_func=ownNFTs)
app.add_url_rule('/<string:contract_address>/<string:tid>',  methods=["GET", "POST"], view_func=ownNFTDetails)


@app.route('/')
def index():
    # return render_template('index.html')
    return render_template('index.html')


@app.route('/ProcessMachineInfo/<string:path>', methods=['POST'])
def ProcessMachineInfo(path):
    # pass file name and the json to deployNFT
    deployMachine.deploy_machine_nft(path)
    return('/')

@app.route('/TransferMachineOwnership/<string:doctorAddress>', methods=['POST'])
def TransferMachineOwnership(doctorAddress):
    if request.method == "POST":
        transferOwnership.transfer_machine_ownership_to_doctor(doctorAddress)
        redirect(url_for('index'))
    return('/')

@app.route('/TransferMachineToPatient/<string:inputInfo>', methods=['POST'])
def TransferMachineOwnershipToPatient(inputInfo):
    transferOwnership.transfer_machine_ownership_to_patient(json.dumps(json.loads(inputInfo), indent=2))
    return('/')

@app.route('/ProcessFilesInfo/<string:inputInfo>', methods=['POST'])
def ProcessFilesInfo(inputInfo):
    # pass the multiple files data and do something with it
    deployMachineData.deploy_nfts(inputInfo)
    return('/')    

@app.route('/ProcessPrescription/<string:inputInfo>', methods=['POST'])
def ProcessPrescription(inputInfo):
    # pass prescription data and do something with it
    deployPrescription.deploy_prescription_nft(json.dumps(json.loads(inputInfo), indent=2))
    return('/')  

@app.route('/ProcessPatient/<string:inputInfo>', methods=['POST'])
def ProcessPatient(inputInfo):
    deployPatient.register_new_patient(json.dumps(json.loads(inputInfo), indent=2))
    return('/') 

@app.route('/registerMachine', methods=['GET'])
def registerMachine():
    return render_template('registerMachine.html')

@app.route('/deployPatient', methods=['GET'])
def deployPatientData():
    return render_template('registerPatient.html')

@app.route('/issuePrescription', methods=['GET'])
def issuePrescription():
    return render_template('issuePrescription.html')

@app.route('/manageData', methods=['GET'])
def manageData():
    return render_template('manageData.html')

@app.route('/displayData/<metaDataUrl>', methods=['GET'])
def displayData(metaDataUrl):
    print("displayData()")
    all_plots = execute(metaDataUrl)
    return render_template('displayData.html', allPlots=all_plots)

if __name__ == "__main__":
    app.run(port=3000,debug=True, use_reloader=False)


