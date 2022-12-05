import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import os
from os import listdir
from os.path import isfile, join

import shutil
import requests

def get_file_names_from_folder_path(mypath):
  files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
  return files

def clean_folder(folder_path):
  for f in os.listdir(folder_path):
      os.remove(os.path.join(folder_path, f))

def download_file(url):
  folder_name = 'inputData'
  response = requests.get(url)
  file = open("{}/file.csv".format(folder_name), "wb")
  file.write(response.content)
  file.close()
 

def generate_plots(current_path, file_names):
  for file_name in file_names:

    if file_name == "physclean.csv":
      continue

    data = pd.read_csv('{}/inputData/{}'.format(current_path, file_name))
    column_names = list(data.columns)

    for column_name in column_names:
      new_plot = data.loc[:, "{}".format(column_name)]

      plt.plot(new_plot.index, new_plot.values)
      plt.xlabel('Measurements')
      plt.ylabel("{}".format(column_name))
      plt.savefig('./img/{}.png'.format(column_name))

def execute(url):
  print("execute()")
  current_path = os.getcwd()
  files_folder_path = '{}/inputData'.format(current_path)
  img_path = '{}/img'.format(current_path)

  clean_folder(img_path)
  clean_folder(files_folder_path)

  print(img_path)
  print(files_folder_path)

  download_file(url)
  file_names = get_file_names_from_folder_path(files_folder_path)
  generate_plots(current_path, file_names)


if __name__ == "__main__":
  execute("https://ipfs.io/ipfs/QmevinMfbqDdTYUDuwoWCe38imCYnEyXHKJM7gGX5VXDAo")