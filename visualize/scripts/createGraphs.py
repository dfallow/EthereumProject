import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt


def generate_plots(file_name):
  data = pd.read_csv('./inputData/{}'.format(file_name))
  column_names = list(data.columns)


  for column_name in column_names:
    new_plot = data.loc[:, "{}".format(column_name)]

    plt.plot(new_plot.index, new_plot.values)
    plt.xlabel('Measurements')
    plt.ylabel("{}".format(column_name))
    plt.savefig('./img/{}.png'.format(column_name))

# generate_plots('pld.csv')
# generate_plots('brp.csv')
# generate_plots('physclean.csv')