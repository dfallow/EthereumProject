import json
from library import ipfs, deployContracts, newContractDetails, mintNFTs


def deploy_contract():
    contract, address = deployContracts.compile_and_deploy_contract(
        newContractDetails.abi, 
        newContractDetails.bytecode
        )
    return contract, address


## 1. uploads machine file to ipfs
## 2. mints the returned hash as url
def register_machine_v1(machine_file_path, contract, address):

    machine_hash = ipfs.store_file(machine_file_path)

    mintNFTs.mint_nft(contract, machine_hash)

    return machine_hash, contract, address

machine_contract, contract_address = deploy_contract()

# machine_file -> path to file
machine_hash, contract, address = register_machine_v1(
    "/home/dfallow/app.js",
    machine_contract,
    contract_address
    )

print("HASH", machine_hash)
print("HASH", contract)
print("HASH", address)


