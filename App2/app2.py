from flask import Flask, render_template, url_for, request, redirect
from web3 import Web3
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join('..')))

from App2 import handleActivity, handleTransaction, browseNFTs, handleActivityDetails

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
  print("ANOTHER PAGE", cType)
  
  transactionDetails = handleActivityDetails.getTransactionDetails(w3, typeOfContract, txn_hash)
  
  
  return render_template("transactionDetails.html", details=transactionDetails)

def ownNFTs():
  return render_template("OwnNFT.html")
  


# if __name__ == "__main__":
#   app2.run(debug=True)
#   app2.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
  
#  python3.10 -m flask --app app2 --debug run --host 0.0.0.0 --port 4444