from flask import Flask, render_template, url_for, request, redirect
from web3 import Web3
import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join('..')))

from App2 import handleTransaction

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))


# #  methods=["GET", "POST"]
# @app.route('/transact')
def transact():
  handleTransaction.main(w3)
  if request.method == "POST":
    nft = request.form.get("nft")
    recipient = request.form.get("recipient")
    key = request.form.get("key")
    
    if not nft or not recipient or not key:
      error = "all form fields required..."
      return error
    print(f"key: {key}, recipient: {recipient}, nft: {nft}")
    return redirect(url_for('transact'))
  
  return render_template("transact.html")

# if __name__ == "__main__":
#   app2.run(debug=True)
#   app2.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
  
#  python3.10 -m flask --app app2 --debug run --host 0.0.0.0 --port 4444