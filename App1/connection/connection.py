from flask import Flask, render_template, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/ProcessInfo/<string:inputInfo>', methods=['POST'])
def ProcessInfo(inputInfo):
  inputInfo = json.loads(inputInfo)
  print()
  print(inputInfo)
  print()
  return('/')

if __name__ == "__main__":
  app.run(debug=True)