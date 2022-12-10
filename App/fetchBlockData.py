from flask import Flask, render_template, url_for, request, redirect
from web3 import Web3
import collections
import handleActivity
import handleActivityDetails
import handleOwnNFT
import handleSingleTokenActivity
import handleSingleUserActivity
import handleMetaData

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
w3.eth.default_account = w3.eth.accounts[0]

async def medicalActivity():
  # get all valid transaction history on the chain
  allActivity = await handleActivity.getMedicalActivity(w3)
  
  txn_hash = request.args.get("tx")
  global cType 
  cType = request.args.get("cType")
  global tidForTransactionDetails
  tidForTransactionDetails = request.args.get("tid")
  
  if txn_hash is not "" and txn_hash is not None:
    print(txn_hash)
    print(cType)
    return redirect(f'/tx/{txn_hash}')
  
  return render_template("medicalActivity.html", Activity=allActivity)

async def txDetails(txn_hash):
  # get these info whe user click the txn_hash in all activity page
  typeOfContract = cType
  tokenId = tidForTransactionDetails
  transactionDetails = await handleActivityDetails.getTransactionDetails(w3, typeOfContract, txn_hash)
  
  caForContractAddressDetails = request.args.get("caForContractAddressDetails")
  if caForContractAddressDetails is not None: 
    return redirect(f'/ca/{caForContractAddressDetails}')
  
  
  return render_template("transactionDetails.html", details=transactionDetails, tid=tokenId)

async def caDetails(contract_address):
  
  allActivity = await handleActivity.getMedicalActivity(w3)
  allActivity = list(filter(lambda x: x.ca == contract_address, allActivity))
  
  txn_hash = request.args.get("tx")
  global cType 
  cType = request.args.get("cType")
  global tidForTransactionDetails
  tidForTransactionDetails = request.args.get("tid")
  
  # only navigate to transaction details page if user click the single activity
  if txn_hash is not "" and txn_hash is not None:
    return redirect(f'/tx/{txn_hash}')
  
  return render_template("contractAddressDetails.html", 
                         contractAddress=contract_address,
                         Activity=allActivity)

def fakeLogin():
  
  global currentUserAddress
  currentUserAddress = request.args.get("acc_num")
  global userAvatar
  userAvatar = request.args.get("avatar")
  global userIdentity
  userIdentity = request.args.get("id")
  
  if currentUserAddress or userAvatar or userIdentity:
    return redirect('/ownnft')
  
  gan_acc = w3.eth.accounts[:5]
  
  avatar = {
    0: "Doctor.png",
    1: "patient1.png",
    2: "patient2.png",
    3: "patient3.png",
    4: "Manufacturer.png",
  }
  
  identity = {
    0: "Doctor",
    1: "Patient",
    2: "Patient",
    3: "Patient",
    4: "Manufacturer"
  }
  
  account = collections.defaultdict(list)
  
  for i, e in enumerate(gan_acc):
    account[e].append(avatar[i])
    account[e].append(identity[i])
    
  
  return render_template("fakeLogin.html", accounts=account)

async def ownNFTs():
  
  try:
    user_acc = currentUserAddress
    w3.eth.default_account = user_acc
    user_avatar = userAvatar
  except:
    return redirect('/login')
  else:
    user_acc = currentUserAddress
    w3.eth.default_account = user_acc
    user_avatar = userAvatar
  
  md, pd, pred, dd = await handleOwnNFT.getOwnNFTs(w3)
  nob = len(md)+len(pd)+len(pred)+len(dd)
  
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
  global numOfToken
  numOfToken = request.args.get("tokenNum")
  
  if numOfToken:
    print("number", numOfToken)
    return redirect('/ownnft/activity')
  
  if contractAddress:
    return redirect(f'/{contractAddress}/{tokenId}')
  
  return render_template("OwnNFT.html", machine=md, 
                         patient=pd, 
                         prescription=pred, 
                         data=dd,
                         avatar=user_avatar,
                         user=w3.eth.default_account,
                         nob=nob)

async def ownNFTDetails(contract_address, tid):
  
  # get all this information from html,
  # when the user click the single nft
  typeoftoken = "" if typeOfToken is None else typeOfToken
  Icon = "" if icon is None else icon
  contractowner = "" if contractOwner is None else contractOwner
  tokenowner = "" if tokenOwner is None else tokenOwner
  datacontractaddress = "" if dataContractAddress is None else dataContractAddress
  prescriptioncontractaddress = "" if prescriptionContractAddress is None else prescriptionContractAddress
  metadataurl = "" if metaDataUrl is None else metaDataUrl
  metadata = [] # for the graph
  itemHistory = [] 
  
  
  if typeOfToken is not None and typeOfToken in ["machine", "prescription", "data"]:
    itemHistory = await handleSingleTokenActivity.getSingleTokenActivity(w3,contract_address, tid, typeOfToken)

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
                         metadata=metadata,
                         Activity=itemHistory,
                         user_address=w3.eth.default_account)
  
async def ownActivity():
  # get the login user info
  user_acc = currentUserAddress
  w3.eth.default_account = user_acc  
  user_avatar = userAvatar
  
  # using the txn hash to view transaction details
  txn_hash = request.args.get("tx")
  global cType 
  cType = request.args.get("cType")
  global tidForTransactionDetails
  tidForTransactionDetails = request.args.get("tid")
  
  # only navigate to transaction details page if user click the single activity
  if txn_hash is not "" and txn_hash is not None:
    return redirect(f'/tx/{txn_hash}')
  
  # num of token the current address (user) owns
  nob = numOfToken
  
  # find all activity related to the current address (user)
  userActivity = await handleSingleUserActivity.getSingleUserActivity(w3)
  
  return render_template('OwnActivity.html', 
                         avatar=user_avatar,
                         user=w3.eth.default_account,
                         nob=nob,
                         Activity=userActivity)
  