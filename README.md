
# EthereumProject

## Project setup

Start in project directory (/EthereumProject)
Run the initial setup script
```
sh InitialSetup.sh
```

### IPFS
To install IPFS, enter these commands:
```
wget https://dist.ipfs.tech/kubo/v0.17.0/kubo_v0.17.0_linux-amd64.tar.gz
tar -xvzf kubo_v0.17.0_linux-amd64.tar.gz

cd kubo
sudo bash install.sh
```

To start IPFS:
```
ipfs init
ipfs daemon
```
### Install Flask

```
source env/bin/activate
pip install flask
```

### Ganache
Currently both the website and dapps are running using a Ganache test chain
* Install Ganache (can download it from [here](https://trufflesuite.com/ganache/))
* Use Quickstart in Ganache to open a new workspace

## Running the website

 1. To launch the website run connection.py (EthereumProject/App/connection/connection.py)
 2. Make sure IPFS is running (run ```ipfs daemon``` in another terminal)
 3. Visit the IP address provided in the terminal after connection.py launches
 4. On the website for doctor and patient addresses use any of the default addresses provided in Ganache workspace

## Running decentralized applications (dapps)

### Setup

* run the command
```
sudo python3 setup.py install
```
* All dapps are located in /EthereumProject/dapps/
* Dapp functionality is contained within a library located in /EthereumProject/library/

### registerMachine.py (dapp1)
1. Run File
   - Console will show a list of account addresses to use (they are the same as the ones in Ganache workspace)
2. Deploy/Transfer Contract
   - Input account address for the manufacturer -> they deploy the contract on the blockchain
   - Deploy contract before continuing
   - After that transferring of contract ownership is done using the same input field
3. Register Machine -> Create/Mint Machine NFT
   - Enter path to the file you are associating the machine with
   - Click "Register Machine"
	   - This will upload machine file to IPFS and mint an NFT associated to it to the blockchain
   - Information shows on right side and in console
4. Transfer Token/NFT ownership
   - Enter account address of the new NFT owner
   - Enter Token ID
   - Click "Transfer Token"

### createPrescription.py (dapp2)
1. Run the file
   - Console will show a list of account addresses to use
2. Deploy Contract
   - Enter Patient Account address  -> Deploys/Owns the contract
   - Enter Doctor Account address -> Associated with the Contract/Patient
   - Click "Deploy Contract"
3. Create Prescription NFT
   - Enter path to the file containing prescription information
   - Enter Machine Token ID -> The machine NFT that the prescription is registered to
   - Click "Create Prescription"
	   - This will upload prescription file to IPFS and mint an NFT associated to it to the blockchain


### uploadMachineFiles.py (dapp3)
1. Run the file
   - Console will show a list of account addresses to use
2. Deploy Contract
   - Enter Patient Account address -> Deploys/Owns their own contract/files
   - Enter Doctor Account address -> Associated with Patient
3. Upload Files
   - Enter Machine Hash -> Reference to file location on IPFS (CID)
   - Enter Machine Token ID -> The machine which produces these files
   - Enter Prescription Token ID -> The Prescription NFT that is associated with the Machine producing the data files
   - Enter path to directory containing files to upload (e.g. ../path/to/dir/ )
   - Click "Upload Files"
	   - This will upload files to IPFS and mint NFTs for each of them
4. Transfer Contract ownership
   - Enter account address to transfer the ownership of contract to
5. Transfer NFT ownership
   - Enter the account address of the new owner
   - Enter a select number of NFT Token IDs to transfer to the account (e.g. 1,3,6 )  
   - Click "Transfer NFTs"
   

### addNewPatient.py (dapp4)
1. Run the file
   - Console will show a list of account addresses to use
2. Deploy Contract
   - Enter Doctor Account address -> Deploys/owns Contract
   - Click "Deploy Contract"
3. Add Patient
   - Enter Patient Account address -> Patient is associated with this Doctor
   - Click "Add New Patient"
	   - This will check whether patient account address is already registered
		   - If yes, it will return data contract and prescription contract addresses on the blockchain associated with this patient
		   - If no, new data and prescription contracts will be deployed to the blockchain and their addresses will be returned

###  getContractNFTs.py (dapp5)
1. Run the file
2. Select contract type
3. Click "Get Contract History"
4. History for that contract appears in the text box
