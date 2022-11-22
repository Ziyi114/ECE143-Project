import pandas as pd
import collections


def get_waittimeAvg(df3):
    """
    this function is to calculate the average time of waiting
    :param df3: pd.DataFrame
    :rtype: float
    """
    assert isinstance(df3, pd.DataFrame)
    waitave_dic = collections.defaultdict(list)
    for car in df3.iterrows():
        key = car[1][0] * 12 + car[1][1] // 5
        waitave_dic[key].append((car[1][2] - car[1][0]) * 60 + car[1][3] - car[1][1])
    for key in waitave_dic:
        waitave_dic[key] = sum(waitave_dic[key]) / len(waitave_dic[key])
    waitave = collections.defaultdict(int)
    for i in range(288):
        waitave[i] = waitave_dic[i]
    for i in range(288):
        if not waitave[i]:
            waitave[i] = waitave[(i - 1) % 288] - 5
            if waitave[i] <= 0:
                waitave[i] = 0
        waitave[i] = round(waitave[i], 4)
    return waitave
