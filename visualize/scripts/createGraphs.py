import pandas as pd
import os
from os import listdir
from os.path import isfile, join

import json
import requests
import numpy as np
import mne

DATA_FOLDER_NAME = "inputData"
DATA_FILE_NAME = "file.edf"

def clean_folder(folder_path):
  for f in os.listdir(folder_path):
      os.remove(os.path.join(folder_path, f))


def create_csv_from_edf(edf_file_path, csv_file_path):
  edf = mne.io.read_raw_edf(edf_file_path)
  header = ','.join(edf.ch_names)
  np.savetxt(csv_file_path, edf.get_data().T, delimiter=',', header=header)


def download_data_file(meta_data_url):
  meta_data_response = requests.get(meta_data_url)
  meta_data_object = json.loads(meta_data_response.content)

  csv_data_url = meta_data_object["image"]
  csv_data_response = requests.get(csv_data_url)

  file = open("{}/{}".format(DATA_FOLDER_NAME, DATA_FILE_NAME), "wb")
  file.write(csv_data_response.content)
  file.close()
 

def get_plot_objects_from_csv(csv_file_path):
    current_path = os.getcwd()
    data = pd.read_csv(csv_file_path)
    column_names = list(data.columns)

    all_plot_objects = []

    for i in range(len(column_names)):
      new_plot = data.loc[:, "{}".format(column_names[i])]

      new_plot_object = {
        "name": column_names[i],
        "labels": new_plot.index,
        "values": new_plot.values
      }

      all_plot_objects.append(new_plot_object)

    return all_plot_objects  



    


def execute(url):
  current_path = os.getcwd()
  data_folder_path = '{}/{}'.format(current_path, DATA_FOLDER_NAME)
  clean_folder(data_folder_path)

  download_data_file(url)

  edf_file_path = '{}/{}'.format(data_folder_path, DATA_FILE_NAME)
  csv_file_path = '{}/{}'.format(data_folder_path, "data.csv")

  create_csv_from_edf(edf_file_path, csv_file_path)

  return get_plot_objects_from_csv(csv_file_path)

 


if __name__ == "__main__":
  execute("https://ipfs.io/ipfs/QmcBKQ17PEGiUC2jnpHd5cfshGuGGyWXuANozExF7auJPr")