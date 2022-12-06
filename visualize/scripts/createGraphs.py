import pandas as pd
import os
from os import listdir
from os.path import isfile, join

import json
import requests

DATA_FOLDER_NAME = "inputData"

def clean_folder(folder_path):
  for f in os.listdir(folder_path):
      os.remove(os.path.join(folder_path, f))

def download_data_file(meta_data_url):
  meta_data_response = requests.get(meta_data_url)
  meta_data_object = json.loads(meta_data_response.content)

  csv_data_url = meta_data_object["image"]
  csv_data_response = requests.get(csv_data_url)

  file = open("{}/file.csv".format(DATA_FOLDER_NAME), "wb")
  file.write(csv_data_response.content)
  file.close()
 

def execute(url):
  download_data_file(url)
 


if __name__ == "__main__":
  execute("https://ipfs.io/ipfs/QmcBKQ17PEGiUC2jnpHd5cfshGuGGyWXuANozExF7auJPr")