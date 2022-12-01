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
1. Run the file
2. Console will show a list of tester account (use these)
3. Input account for the manufacturer -> they deploy the contract
4. Deploy contract before continuing
5. Enter path to the file you are associating the machine with
6. Information is displayed at bottom, and more in the terminal

### createPrescription.py (daap2)
1. Run the file
2. Console will show a list of tester account (use these)
3. This app needs to be modifie, so the insturctions won't be completed now


### uploadMachineFies.py(dapp3)
1. Run the file
2. Console will show a list of tester account (use these)
3. Input account for the patient -> they deploy the contract
4. Input doctor account -> they are registered with the contract
5. Deploy contract before continuing
6. Enter the following
   - Hash of machine file from IPFS (retrieved from dapp1)
   - Machine Token/NFT ID (retrieved from dapp1)
   - Prescription Token/NFT ID (retrived from dapp2) (since dapp2 is incomplete can be any int)
   - Path to the directory containing the files you want to upload
7. Information displayed in terminal

### addNewPatient (dapp4)
1. Run the file
2. Console will show a list of tester account (use these)
3. Input account for the doctor -> they deploy the contract
4. Deploy contract before continuing
5. Enter the following
   - Patient account
   - Data Contract Address (associated with patient, retrieved from daap3)
   - Prescription Contract Address (associated with patient, retrieved from daap2)
6. Information is displayed in the terminal







