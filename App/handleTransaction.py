import contractDetailsMachineToken as cd
from web3 import Web3
import json
from urllib.request import urlopen


class NFTs:
    def __init__(
        self, contractAddress: str,
        ipfs_metadata: str,
        img_ipfs: str,
        name: str,
        collection: str,
        tokenId: int,
        owner: str,
    ):
        self.contractAddress = contractAddress
        self.ipfs_metadata = ipfs_metadata
        self.img_ipfs = img_ipfs
        self.name = name,
        self.collection = collection
        self.tokenId = tokenId
        self.owner = owner

# get the NFTs a user owns


def getMyNFTs(w3):
    # w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
    w3.eth.default_account = w3.eth.accounts[0]

    numOfBLK = w3.eth.get_block('latest')["number"]

    allContractAddress = list(set([
        w3.eth.get_transaction(w3.eth.get_block(
            i)["transactions"][0].hex())["to"]
        for i in reversed(range(1, numOfBLK+1))
        if w3.eth.get_transaction(w3.eth.get_block(i)["transactions"][0].hex())["to"] is not None
    ]))

    myNFTs_data = []

    for ca in allContractAddress:
        contract = w3.eth.contract(address=ca, abi=cd.abi)
        numOfNFTs = contract.functions.totalSupply().call()
        print(numOfNFTs)

        # for i in range(numOfNFTs):
        #     print(contract.functions.tokenIdToOwner(i+1).call())

        # # print(contract.fun)

        if w3.eth.default_account in list(set([contract.functions.tokenIdToOwner(x+1).call() for x in range(numOfNFTs)])):
            ownedToken = [
                x
                for x in range(numOfNFTs)
                if contract.functions.tokenIdToOwner(x+1).call() == w3.eth.default_account
            ]

            for num in ownedToken:
                metadata = contract.functions.dataItems(num).call()[-1]
                print(json.loads(urlopen(metadata).read())["image"])

                myNFTs_data.append(
                    NFTs(ca,
                         metadata,
                         json.loads(urlopen(metadata).read())["image"],
                         json.loads(urlopen(metadata).read())["name"],
                         json.loads(urlopen(metadata).read())[
                             "attributes"][0]["department"],
                         num + 1,
                         contract.functions.tokenIdToOwner(num+1).call(),
                         )
                )

    return myNFTs_data

    # target_block = w3.eth.get_block(6)
    # print("Block details: ", target_block)

    # txh = target_block["transactions"][0].hex()
    # print("Transaction hash: ", txh)

    # # get transaction
    # transaction = w3.eth.get_transaction(txh)
    # print("Transaction details: ", transaction)

    # c_add = transaction["to"]
    # contract = w3.eth.contract(address=c_add, abi=cd.abi)

    # numOfNFTs = contract.functions.totalSupply().call()

    # print("number of NFTs in this collections", numOfNFTs)

    # return [json.loads(urlopen(contract.functions.dataItems(i).call()[-1]).read())["image"]
    #     for i in range(numOfNFTs)]

    # print(contract.functions.dataItems(0).call())
    # print(contract.functions.dataItems(1).call())

    # print("OWNERSHIP", contract.functions.getOwnerOfToken(1).call() )
    # c_data =
    # print(c_data)

    # metadata = json.loads(urlopen(c_data[-1]).read())
    # print("https://ipfs.io/ipfs/" + metadata["imageUrl"])
