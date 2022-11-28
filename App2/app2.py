from flask import Flask, render_template, url_for, request, redirect, session
from web3 import Web3
import json
import os
import sys
import timeit
sys.path.append(os.path.abspath(os.path.join('..')))

from App2 import handleTransaction, browseNFTs, nftTransfer, browseCollection, singleCollectionActivity

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

# this default account represent the current user
# can transfer his NFT
w3.eth.default_account = w3.eth.accounts[1]

# #  methods=["GET", "POST"]
# @app.route('/transact')
def transact():
  
  getMyNfts = handleTransaction.getMyNFTs(w3)
  
  if request.method == "POST":
    nft = request.form.get("tid")
    recipient = request.form.get("to_acc")
    contract = request.form.get("contract")
    privateKey = request.form.get("p_key")
    
    if not nft or not recipient or not contract:
      error = "all form fields required..."
      return error
    print(f"recipient: {recipient}, nft: {nft}, contract: {contract}")
    
    # do the transaction here
    nftTransfer.transferOwnerOfNFT(w3, nft, contract, recipient, privateKey)
    return redirect(url_for('transact'))
  
  return render_template("transact.html", myNFTs=getMyNfts)

def browsingPage():
  # display the first nft of a collection
  # reduce the loading time
  getAllCollections = browseNFTs.getAllNFTsCollections(w3)
  
  # when the nft is clicked, it redirects to a page 
  # where contains all the nfts of the collection
  if request.method == "GET":
    ca = request.args.get("ca")
    collection = request.args.get("collections")
    if collection is not None: return redirect(f'/browseNFTs/collection/{ca}/{collection}')
    
  
  return render_template("BrowseNFTs.html", collections=getAllCollections)

def singleCollection(contractAddress, collection):
  creator = browseCollection.getSmartContractCreator(w3, contractAddress) 
  nfts = browseCollection.getNFTsBySmartContract(w3, contractAddress) 
  
  
   
  return render_template("singleCollection.html", 
                         c_name=collection,
                         creator=creator,
                         NFTs=nfts)
  
  

# if __name__ == "__main__":
#   app2.run(debug=True)
#   app2.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
  
#  python3.10 -m flask --app app2 --debug run --host 0.0.0.0 --port 4444