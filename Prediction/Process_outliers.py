from statistics import mean, stdev


def Process_outliers(X, y):
    """
    this function is to process our dataset to drop some outliers of the dataset
    in order to get better performance

    :param X: list, features
    :param y: list, labels
    :rtype: list, list
    """
    upper = mean(y) + 1.5 * stdev(y)
    lower = mean(y) - 1.5 * stdev(y)
    X_process = []
    y_process = []
    for i in range(len(y)):
        X_process.append(X[i])
        if lower < y[i] < upper:
            y_process.append(y[i])
        else:
            y_process.append(0)
    for i in range(len(y_process)):
        if y_process[i] == 0:
            tmp = []
            k = 0
            for j in range(1, 4):
                while y_process[(i + j + k) % len(y_process)] == 0:
                    k += 1
                tmp.append(y_process[(i + j + k) % len(y_process)])
            for j in range(1, 4):
                while y_process[(i - j - k) % len(y_process)] == 0:
                    k += 1
                tmp.append(y_process[(i - j - k) % len(y_process)])
            y_process[i] = sum(tmp) / len(tmp)
    return X_process, y_process
