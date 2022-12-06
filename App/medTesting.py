from web3 import Web3
from urllib.request import urlopen
from datetime import datetime
import collections


import contractDetailsMachineToken as mta
import contractDetailsPatientToken as pta
import contractDetailsPrescriptionToken as preta
import contractDetailsDataToken as dta



w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

w3.eth.default_account = w3.eth.accounts[1]

caToBytecode = {}

numOfBLK = w3.eth.block_number
# print(numOfBLK)


# print("old timestamp ", w3.eth.get_block(1).timestamp)
# print("now timestamp ", datetime.timestamp(datetime.now()))
# date = datetime(2022,3,27,13,27,45,46000) 
# date1 = datetime.fromtimestamp(w3.eth.get_block(1).timestamp)
# date2 = datetime.fromtimestamp(datetime.timestamp(datetime.now()))
# print("date ", date1)
# print("date2 ", date2)

# print((date2-date1).seconds)


avatar = {
    0: "https://ipfs.io/ipfs/Qmemr6XQy7DqKi6q8SM6XuhJ6VSvEmktYHhvsUPpwWg3Wz",
    1: "https://ipfs.io/ipfs/QmSqhAwm5Yqdyf8Smkp3hpMt7gShDDEa27R51gR14qU7up",
    2: "https://ipfs.io/ipfs/QmPrGrmwkrPEUdyw3A2eoQtysBV8MsZ13VgBt7P4YVaeH9",
    3: "https://ipfs.io/ipfs/QmdVJ34h6GJzsrmxpVuqHvMrembxqpM3Xrtcn7GVnHYWCA",
    4: "https://ipfs.io/ipfs/QmS7rfZQjG135AwpuKjcVkFRgPJ6Fgk5rcYrPKtAfn6T4u",
}
  
identity = {
    0: "doctor",
    1: "patient",
    2: "patient",
    3: "patient",
    4: "manufacturer"
}
  
account = collections.defaultdict(list)
  
for i, e in enumerate(w3.eth.accounts):
    account[e].append(avatar[i])
    account[e].append(identity[i])
    
for acc in account:
    print(account[acc][0])

# if timestamp day > 0 then show days
# else if second < 60 then n second ago
# if second > 60 then / 60 then n mins ago
# if 


# print(type(date2-date1))


# for n in range(1, numOfBLK+1):
#     if (w3.eth.get_transaction(w3.eth.get_block(n)["transactions"][0].hex())["to"] == None and
#     w3.eth.get_transaction_receipt(w3.eth.get_block(n)["transactions"][0].hex())["contractAddress"] not in caToBytecode):
#         ca = w3.eth.get_transaction_receipt(w3.eth.get_block(n)["transactions"][0].hex())["contractAddress"]
#         bc = w3.eth.getTransaction(w3.eth.get_block(n)["transactions"][0].hex())["input"]
#         #print("\nBC", bc )
#         caToBytecode[ca] = bc

# # print(preta.bytecode)

# for i in caToBytecode:
#     print(i)
#     if caToBytecode[i] == "0x" + mta.bytecode:
#         print("machine")
#     elif caToBytecode[i] == "0x" + pta.bytecode:
#         print("patient")
#     elif caToBytecode[i][:(len(caToBytecode[i])-64)] == "0x" + preta.bytecode:
#         print("prescription")
#     elif caToBytecode[i][:(len(caToBytecode[i])-64)] == "0x" + dta.bytecode:
#         print("data")


# allValidTxh = [w3.eth.get_block(n)["transactions"][0].hex()
#                for n in range(1, numOfBLK+1)]

# txh = w3.eth.getTransaction(allValidTxh[2])
# ca = txh["to"]
# print(txh["hash"].hex())
# print(txh["blockNumber"])
# print(txh["from"])
# print(txh["to"])

# contract = w3.eth.contract(address=ca, abi=mta.abi)

# numOfToken = contract.functions.totalMachineTokens().call()

# print("NUMBER OF MACHINE TOKEN ", numOfToken)

# for n in range(1, numOfToken+1):
#     print(f"OWNER of TOKEN {n}: ", contract.functions.getTokenOwner(n).call())

# print(contract.functions.tokenURI(2).call())
# print("\n")


# patient
# txh = w3.eth.getTransaction(allValidTxh[7])
# ca = txh["to"]
# print(ca)
# contract = w3.eth.contract(address=ca, abi=pta.abi)
# patientContractOwner = contract.functions.owner().call() #doctor
# print(patientContractOwner)
# print("number of patient", contract.functions.numberOfPatients().call())
# w3.eth.default_account = w3.eth.accounts[0]
# allPatient = contract.functions.getAllPatients().call()
# print(allPatient)
# print(allPatient[0][0])
# print(allPatient[1][0])
# print(allPatient[2][0])

# tg = [[1, 2, 3], [1, 2], [1, 2]]

# print(tg[0])


# prescription
# txh = w3.eth.getTransaction(allValidTxh[11])
# ca = "0x34bb3DF4db6f0b8F383b5B368E63C83314660A10"
# contract = w3.eth.contract(address=ca, abi=dta.abi)
# owner = contract.functions.owner().call()
# print(owner)
# doctor = contract.functions.getDoctor().call()
# print(doctor)
# numOfTokens = contract.functions._numberOfDataTokens().call()
# print(numOfTokens)

# item = contract.functions.tokenURI(1).call()
# print(item)
# prescriptionOwner = contract.functions.owner().call()
# print(prescriptionOwner)
# token = contract.functions.tokenURI(1).call()
# try:
#     token = contract.functions.tokenURI(1).call()
#     print(token)
#     req = urlopen("http://bafybeibard5ahnzi3zjbyepm4uxsrtbpo6rnle2svwk6jxbievb2i3n2uy.ipfs.localhost:8080/")
#     md_json = json.loads(req.read())
#     req.close()
#     print(md_json)
#     print(md_json["patient"])
# except:
#     pass
# numOfToken = contract.functions.numberOfPrescriptionTokens().call()
# print(numOfToken)
# nft = contract.functions.tokenURI(1).call()
# print(nft)

# 0x846CA53CcEE308F5065059D1f2E3037E48E31548
