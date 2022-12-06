from flask import Flask, render_template, url_for, request, redirect
from web3 import Web3
import handleActivity
import handleTransaction
import browseNFTs
import handleActivityDetails
import handleOwnNFT
import handleMetaData

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
w3.eth.default_account = w3.eth.accounts[1]

# #  methods=["GET", "POST"]
# @app.route('/transact')
def transact():
  if request.method == "POST":
    nft = request.form.get("nft")
    recipient = request.form.get("recipient")
    key = request.form.get("key")
    contract = request.form.get("contract")
    
    if not nft or not recipient or not key or not contract:
      error = "all form fields required..."
      return error
    print(f"key: {key}, recipient: {recipient}, nft: {nft}, contract: {contract}")
    return redirect(url_for('transact'))
  
  return render_template("transact.html", myNFTs=handleTransaction.getMyNFTs(w3))

def browsingPage():
  return render_template("BrowseNFTs.html", allNFTs=browseNFTs.getAllNFTs())

async def medicalActivity():
  # get all valid transaction history on the chain
  allActivity = await handleActivity.getMedicalActivity(w3)
  
  txn_hash = request.args.get("tx")
  global cType 
  cType = request.args.get("cType")
  
  if txn_hash is not "" and txn_hash is not None:
    print(txn_hash)
    print(cType)
    return redirect(f'/tx/{txn_hash}')
  
  return render_template("medicalActivity.html", Activity=allActivity)

def txDetails(txn_hash):
  typeOfContract = cType
  transactionDetails = handleActivityDetails.getTransactionDetails(w3, typeOfContract, txn_hash)
  
  
  return render_template("transactionDetails.html", details=transactionDetails)

async def ownNFTs():
  md, pd, pred, dd = await handleOwnNFT.getOwnNFTs(w3)
  
  # essential for access details page
  contractAddress = request.args.get("ca")
  tokenId = request.args.get("tid")
  
  # another variables for specific page
  global typeOfToken
  typeOfToken = request.args.get("type")
  global icon
  icon = request.args.get("icon")
  global contractOwner
  contractOwner = request.args.get("c_owner")
  global tokenOwner
  tokenOwner = request.args.get("owner")
  global dataContractAddress
  dataContractAddress = request.args.get("dca")
  global prescriptionContractAddress
  prescriptionContractAddress = request.args.get("preca")
  global metaDataUrl
  metaDataUrl = request.args.get("md_url")
  
  if contractAddress:
    return redirect(f'/{contractAddress}/{tokenId}')
  
  # contractAddress
  
  
  
  return render_template("OwnNFT.html", machine=md, patient=pd, prescription=pred, data=dd)

async def ownNFTDetails(contract_address, tid):
  
  
  typeoftoken = "" if typeOfToken is None else typeOfToken
  Icon = "" if icon is None else icon
  contractowner = "" if contractOwner is None else contractOwner
  tokenowner = "" if tokenOwner is None else tokenOwner
  datacontractaddress = "" if dataContractAddress is None else dataContractAddress
  prescriptioncontractaddress = "" if prescriptionContractAddress is None else prescriptionContractAddress
  metadataurl = "" if metaDataUrl is None else metaDataUrl
  
  metadata = []
  
  # if typeOfToken in [""]
  
   
  
  return render_template("OwnNFTDetails.html",
                         contractAddress=contract_address,
                         tokenId=tid,
                         typeOfToken=typeoftoken,
                         icon=Icon,
                         contractOwner=contractowner,
                         tokenOwner=tokenowner,
                         dataContractAddress=datacontractaddress,
                         prescriptionContractAddress=prescriptioncontractaddress,
                         metaDataUrl=metadataurl,
                         metadata=metadata
                         )
  


# if __name__ == "__main__":
#   app2.run(debug=True)
#   app2.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
  
#  python3.10 -m flask --app app2 --debug run --host 0.0.0.0 --port 4444