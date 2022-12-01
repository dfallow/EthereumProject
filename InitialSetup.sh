#! usr/bin/bash

sudo apt-get update
sudo apt-get install python3.6
sudo apt install python3-pip

sudo snap install ipfs

pip install ipfs-api
pip install "web3[tester]"
pip install eth-tester
pip install py-evm

sudo apt-get update
sudo apt install nodejs npm
npm install
