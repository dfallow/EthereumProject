from flask import Flask, render_template, url_for
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import deployNFT
## Returns /home/dfallow/Documents/EthereumProject
app_one_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
os.chdir(app_one_dir)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/ProcessInfo/<string:inputInfo>', methods=['POST'])
def ProcessInfo(inputInfo):
  inputInfo = json.loads(inputInfo)

  info_object = json.dumps(inputInfo, indent=2)

  ##with open(app_one_dir + "/tempFiles/test.json", "x") as file:
  ##  file.write(info_object)
  deployNFT.deploy_nft()

  print(info_object)
  print()
  print(inputInfo)
  print()
  
  return('/')

if __name__ == "__main__":
  app.run(debug=True)