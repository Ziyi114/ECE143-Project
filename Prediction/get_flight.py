import pandas as pd
import collections


def get_flight(Path):
    """
    this function is to get flight data, and process yhe data

    :param Path: str
    :rytpe: pd.DataFrame, collections.defaultdict
    """
    assert isinstance(Path, str)
    assert len(Path) > 0
    assert Path[-4:] == '.csv'
    df = pd.read_csv('U://Programming for Data Science (ECE143 22fall)//Final Project//flight.csv')
    time = df.loc[:, 'SCHEDULED ARRIVAL']
    timelist = []
    for i in time:
        timelist.append(i[:5])
    dic = collections.defaultdict(int)
    for time in timelist:
        tmp = int(time[:2]) * 12 + int(time[-2:]) // 5
        dic[tmp] += 1
    return df, dic
