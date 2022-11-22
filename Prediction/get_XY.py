def get_XY(df3, carNumTable1, dic, waitave):
    """
    this function is to get our features X and our labels y

    :param dic: flight info dictionary
    :param df3: pd.DataFrame
    :param carNumTable1: pd.DataFrame
    :param waitave: average wait-time
    :rtype: list,list
    """
    assert isinstance(df3, pd.DataFrame)
    assert isinstance(carNumTable1, pd.DataFrame)
    X = []
    y = []
    for car in df3.iterrows():
        x1 = car[1][0] * 12 + car[1][1] // 5
        x2 = carNumTable1[1][x1]
        x3 = \
            dic[(x1 - 4) % 288] + dic[(x1 - 3) % 288] + \
            dic[(x1 - 2) % 288] + dic[(x1 - 1) % 288] + \
            dic[x1] + \
            dic[(x1 + 1) % 288] + dic[(x1 + 2) % 288] + \
            dic[(x1 + 3) % 288] + dic[(x1 + 4) % 288]

        X.append([x1, x2, x3])
        y.append(waitave[x1])
    return X, y
