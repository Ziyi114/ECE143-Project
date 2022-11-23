import numpy as np
import matplotlib.pyplot as plt
import collections
from sklearn.model_selection import train_test_split


def get_set(X, y):
    """
    this function is to divide our X and y into trainning and testing sets
    :param X: list, features set
    :param y: list, labels
    :rtype: tuple
    """
    assert isinstance(X, list)
    assert isinstance(y, list)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test


def plot_EstimateOnApr1st(T_r, ave_rev, running_portions, waitave_process):
    """
    This function shows a comparison of estimated profits between waiting
    in the airport and going back to urban area
    :param T_r: time of going back to urban area
    :param ave_rev: average revenue
    :param running_portions: loaded rate of taxi in urban area
    :param waitave_process: wait-time
    :return: plots
    """
    x = np.arange(288)
    P_w = []
    P_d = []
    for i in x:
        P_d.append(waitave_process[i] / 60 * ave_rev[i // 12] * running_portions[i] - 0.12 * waitave_process[i])
        P_w.append(T_r * ave_rev[i // 12] / 60)
    plt.figure(figsize=(20, 10))
    plt.plot(x, P_d, 'r')
    plt.plot(x, P_w, 'g')
    plt.legend(['Estimated departure profit', 'Estimated wait profit'])


def get_EstimateOnTestSet(model,X_process, y_process, ave_rev, running_portions, T_r):
    """
    This functino runs our estimation models on testing set and
     shows the comparison between estimated profit based on predicted wait-time, real wait-time
     and waiting in airport
    :param X_process: 3 features
    :param y_process: real wait-time
    :param ave_rev: average revenues
    :param running_portions: loaded rate
    :param T_r: time of going back to urban
    :return: plots of comparison between estimated profit based on predicted wait-time(blue), real wait-time(red)
     and waiting in airport(green)
    """
    P_w = collections.defaultdict(float)
    P_dr = collections.defaultdict(float)
    P_dp = collections.defaultdict(float)
    X_train, X_test, y_train, y_test = get_set(X_process, y_process)
    predicted_wait = model.predict(X_test)
    for i in range(len(X_test)):
        P_dp[X_test[i][0]] = predicted_wait[i] / 60 * ave_rev[X_test[i][0] // 12] * running_portions[
            X_test[i][0]] - 0.12 * predicted_wait[i]
        P_dr[X_test[i][0]] = y_test[i] / 60 * ave_rev[X_test[i][0] // 12] * running_portions[X_test[i][0]] - 0.12 * \
                             y_test[i]
        P_w[X_test[i][0]] = T_r * ave_rev[X_test[i][0] // 12] / 60

    new_P_dp = sorted(P_dp.items())
    x1, y1 = zip(*new_P_dp)
    new_P_dr = sorted(P_dr.items())
    x2, y2 = zip(*new_P_dr)
    new_P_w = sorted(P_w.items())
    x3, y3 = zip(*new_P_w)

    fig, ax = plt.subplots(figsize=(20, 10))
    # fig.figsize(20,10)

    ax.plot(x1, y1, 'r')
    ax.plot(x2, y2, 'b')
    ax.plot(x3, y3, 'g')
    ax.legend(['Profit based on predicted Y', 'Profit based on real Y', 'Estimated wait profit'])
    print(len(y2), len(y3))
    ax.fill_between(x1, 0, 50, where=np.array(y3) > np.array(y1), color='orange', alpha=0.2, interpolate=True)
    plt.show()
