from flask import Flask, render_template, url_for, request, redirect
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))

import newDeployNFT
import deployMachineData

## Returns /home/dfallow/Documents/EthereumProject
app_one_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
os.chdir(app_one_dir)

# able to access other route from app2 folder
sys.path.append(os.path.abspath(os.path.join('..')))
from App2.app2 import transact, browsingPage

from visualize.scripts.createGraphs import execute

app = Flask(__name__)
app.add_url_rule('/transact', methods=["GET", "POST"], view_func=transact)
app.add_url_rule('/browseNFTs', view_func=browsingPage)
# app.add_url_rule('/browseNFTs/collection/<string:contractAddress>/<string:collection>', methods=["GET", "POST"], view_func=singleCollection)

@app.route('/')
def index():
    # return render_template('index.html')
    return render_template('index.html')


@app.route('/ProcessMachineInfo/<string:inputInfo>', methods=['POST'])
def ProcessMachineInfo(inputInfo):
    # pass file name and the json to deployNFT
    print("NEW DATA", json.loads(inputInfo))
    newDeployNFT.new_deploy_nft(json.loads(inputInfo)['name'],json.dumps(json.loads(inputInfo), indent=2))
    return('/')

@app.route('/ProcessFilesInfo/<string:inputInfo>', methods=['POST'])
def ProcessFilesInfo(inputInfo):
    # pass the multiple files data and do something with it
    deployMachineData.deploy_nfts(inputInfo)
    return('/')    

@app.route('/registerMachine', methods=['GET'])
def registerMachine():
    return render_template('registerMachine.html')

@app.route('/manageData', methods=['GET'])
def manageData():

    return render_template('manageData.html')

@app.route('/showData', methods=['GET'])
def showData():
    current_path = os.getcwd()
    image_names = os.listdir("{}/connection/static/img".format(current_path))
    return render_template('showData.html', image_names=image_names )

@app.route('/ProcessPlotsInfo', methods=['GET'])
def ProcessPlotsInfo():
    execute("https://ipfs.io/ipfs/QmevinMfbqDdTYUDuwoWCe38imCYnEyXHKJM7gGX5VXDAo")


if __name__ == "__main__":
    app.run(port=3000,debug=True, use_reloader=True)
    


