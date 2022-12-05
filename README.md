# EthereumProject

##Project setup

1. Start in project directory (/EthereumProject)
2. Run the initial setup script
```
sh InitialSetup.sh
```

### IPFS
To start ipfs:
```
ipfs init
ipfs daemon
```
Vist ip address in teminal

### Install Flask

```
source env/bin/activate
pip install flask
```

### Running the website

* To launch website run connection.py (EthereumProject/App1/connection/connection.py)
* Check terminal for ip address

## Dapps

### Setup

* run the command
```
sudo python3 setup.py install
```
* Location of dapps (/EthereumProject/dapps/)
* EthereumProject/library contains functionality

### registerMachine.py (dapp1)
1. Run File
   - Console will show a list of accounts to use
2. Deploy/Transfer Contract
   - Input account for the manufacturer -> they deploy the contract
   - Deploy contract before continuing
   - Transferring contract ownership is then done using the same field
3. Register Maching -> Create/Mint Maching NFT
   - Enter path to the file you are associating the machine with
   - Click "Register Machine"
   - Information shows on right side and in console
4. Transfer Token/NFT
   - Enter Account to be transfered to
   - Enter Token ID

### createPrescription.py (daap2)
1. Run the file
   - Console will show a list of accounts to use
2. Deploy Contract
   - Enter Patient Account -> Deploys/Owns Comtract
   - Enter Doctor Account -> Associated with the Contract/Patient
3. Create Prescription NFT
   - Enter path to file containing prescription information
   - Enter Machine Token ID -> The machine NFT that the prescription is registered to


### uploadMachineFies.py(dapp3)
1. Run the file
   - Console will show a list of account
2. Deploy Contract
   - Enter Patient Account -> Deploys/Ows their own contract/files
   - Enter Doctor Account -> Asscoiated with patient
3. Upload Files
   - Enter Maching Hash -> Reference to file location on IPFS
   - Enter Machine Token ID -> The machine which produces these files
   - Enter Prescription Token ID -> Reference to All Contracts/Files
   - Enter path to directory containing files to upload (e.g. ../path/to/dir/ )
4. Transfer Contract
   - Enter Account to transfer ownership of contract to
5. Transfer NFTs
   - Enter the account to transfer to
   - Enter a select number of NFTs Token IDs to transfer to the account (e.g. 1,3,6 )  
   

### addNewPatient.py (dapp4)
1. Run the file
   - Console will show a list of accounts
2. Deploy Contract
   - Enter Doctor Account -> Deploys/owns Contract
3. Add Patient
   - Enter Patient Account -> Patient is associated with this Doctor
4. Input doctor account -> they are registered with the contract

###  getContractNFTs.py (dapp5)
1. Run the file
2. Select contract
   - choose which contract to view history for
   - History appears in the text box after button is clicked
