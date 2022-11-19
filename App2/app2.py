from flask import Flask, render_template, url_for, request, redirect
from web3 import Web3
import json
import os
import sys
import timeit
sys.path.append(os.path.abspath(os.path.join('..')))

from App2 import handleTransaction, browseNFTs, nftTransfer

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

# this default account represent the current user
# can transfer his NFT
w3.eth.default_account = w3.eth.accounts[0]

# #  methods=["GET", "POST"]
# @app.route('/transact')
def transact():
  
  getMyNfts = handleTransaction.getMyNFTs(w3)
  
  if request.method == "POST":
    nft = request.form.get("nft")
    recipient = request.form.get("recipient")
    contract = request.form.get("contract")
    
    if not nft or not recipient or not contract:
      error = "all form fields required..."
      return error
    print(f"recipient: {recipient}, nft: {nft}, contract: {contract}")
    
    # do the transaction here
    nftTransfer.transferOwnerOfNFT(w3, nft, contract, recipient)
    return redirect(url_for('transact'))
  
  return render_template("transact.html", myNFTs=getMyNfts)

def browsingPage():
  getAllNFTs = browseNFTs.getAllNFTs()
  return render_template("BrowseNFTs.html", allNFTs=getAllNFTs)

# if __name__ == "__main__":
#   app2.run(debug=True)
#   app2.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
  
#  python3.10 -m flask --app app2 --debug run --host 0.0.0.0 --port 4444