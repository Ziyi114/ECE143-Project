import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas


def plot(data, title, x_label, y_label):
    """
    plot and vistaulize the raw data of out X matrix of training data

    :param data: data of the plot
    :param title: plot title
    :param x_label: x label of the plot 
    :param y_label: y label of the plot 
    """

    y = []

    if isinstance(data, list):
        y = data
    elif isinstance(data, dict):
        y=[0]*288
        for i in data:
            y[i] = data[i]
    elif isinstance(data, pandas.DataFrame):

        y = [0] * 288
        for i, row in data.iterrows():

            y[i] = row[1]
    width = 1/12
    xlabel = []
    # with open(filename) as csvfile:
    #
    #     plots = csv.reader(csvfile, delimiter=',')
    #     for row in plots:
    #         y.append(eval(row[0]))


    #########
    for i in range(len(y)+1):
        if i % 12 == 0:
            xlabel.append(i//12)
        else:
            xlabel.append("")
    #ind = np.arange(len(y))

    fig, ax = plt.subplots(figsize=(20,10))
    ax.bar(np.arange(0, len(y)/12, 1/12), y, width = 1/12,linewidth=0.1, edgecolor='b')
    ax.set_xlim(-0.1, 24)
    #ax.set_ylim(0, 210)
    ax.set_xticks(list(range(24)))
    ax.set_xticklabels([f"{i}:00" for i in range(24)], rotation=45, fontsize=8)
    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)
    ax.set_title(title, fontsize=16)
    # ax.plot(np.arange(0, len(y)/12, 1/12), y, color="orange")
    # ax.fill_between(np.arange(0, len(y)/12, 1/12), 0, y, where=np.array(y) > 0)
    plt.show()


# if __name__ == '__main__':
#     #plot('Num of car in parking per 5 mins.csv', "Cars count per 5 min", "time", "car count")
#     #plot('flight info per 5 mins.csv', "flight counts per 5 mins", "time", "avetime")
#     plot('waitave per 5 mins.csv', 'wait time average per 5 mins', 'time', 'avetime')
