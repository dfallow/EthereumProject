from flask import Flask, render_template, request
from web3 import Web3
import os

app2 = Flask(__name__,template_folder="html")

@app2.route('/', methods=["GET", "POST"])
def home():
  # showETH()
  if request.method == "POST":
    nft = request.form.get("nft")
    recipient = request.form.get("recipient")
    key = request.form.get("key")
    
    if not nft or not recipient or not key:
      error = "all form fields required..."
      return error
    print(f"key: {key}, recipient: {recipient}, nft: {nft}")
    return('/')
  return render_template("home.html")

# def showETH():
  # print("hi")

if __name__ == "__main__":
  app2.run(debug=True)
  app2.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
  
#  python3.10 -m flask --app app2 --debug run --host 0.0.0.0 --port 4444