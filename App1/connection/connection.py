from flask import Flask, render_template, url_for, request, redirect
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import deployNFT
## Returns /home/dfallow/Documents/EthereumProject
app_one_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
os.chdir(app_one_dir)

# able to access other route from app2 folder
sys.path.append(os.path.abspath(os.path.join('..')))
from App2.app2 import transact

app = Flask(__name__)
app.add_url_rule('/transact', methods=["GET", "POST"], view_func=transact)


@app.route('/')
def index():
  #return render_template('index.html')
  return render_template('addMachine.html')

@app.route('/ProcessInfo/<string:inputInfo>', methods=['POST'])
def ProcessInfo(inputInfo):
  # pass file name and the json to deployNFT
  deployNFT.deploy_nft(json.loads(inputInfo)['name'],json.dumps(json.loads(inputInfo), indent=2))
  return('/')

if __name__ == "__main__":
  app.run(debug=True, use_reloader=True)
  app.run("0.0.0.0")