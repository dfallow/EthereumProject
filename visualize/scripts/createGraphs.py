import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import os

from os import listdir
from os.path import isfile, join

def get_file_names_from_folder_path(mypath):
  files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
  return files

def clean_folder(folder_path):
  for f in os.listdir(folder_path):
      os.remove(os.path.join(folder_path, f))
 

def generate_plots(file_names):
  for file_name in file_names:
    data = pd.read_csv('{}/inputData/{}'.format(current_path, file_name))
    column_names = list(data.columns)

    for column_name in column_names:
      new_plot = data.loc[:, "{}".format(column_name)]

      plt.plot(new_plot.index, new_plot.values)
      plt.xlabel('Measurements')
      plt.ylabel("{}".format(column_name))
      plt.savefig('./img/{}.png'.format(column_name))


current_path = os.getcwd()
files_folder_path = '{}/inputData'.format(current_path)
file_names = get_file_names_from_folder_path(files_folder_path)
clean_folder(files_folder_path)
# generate_plots(file_names)




# data = pd.read_csv('{}/inputData/{}'.format(current_path, file_name))
# column_names = list(data.columns)
# generate_plots(column_names)
