import pandas as pd
import ifInAirportField


def get_all_taxis_data(location):
    """
    this function is to get all the taxi data based on the dataset

    ：param location: str, means the location
    :rtype: pd.DataFrame, list
    """
    assert isinstance(location, str)
    waitTimeDict = {}
    inFieldSet = []
    for hour in range(24):
        for min in range(60):
            path = location + str(hour).zfill(2) + '//180401' + str(hour).zfill(2) + str(min).zfill(2) + '.txt'
            data = pd.read_csv(path, sep='|', header=None, encoding="ISO-8859-1")
            for row in data.itertuples():
                if ifInAirportField.ifInAirportField(row[11], row[12]):
                    if row[1] not in inFieldSet:
                        inFieldSet.append(row[1])
                        waitTimeDict[row[1]] = [hour, min, None, None]
                else:
                    if row[1] in inFieldSet:
                        waitTimeDict[row[1]][2] = int(hour)
                        waitTimeDict[row[1]][3] = int(min)
                        del inFieldSet[inFieldSet.index(row[1])]
    waitTimeDict = pd.DataFrame.from_dict(waitTimeDict, orient='index')
    df2 = waitTimeDict.dropna()  # drop all rows with NaN value
    df3 = df2.astype('int')  # convert all float to int
    index_list = []
    for idx, row in df3.iterrows():
        if row[2] * 60 + row[3] - row[0] * 60 - row[1] <= 2:
            df3 = df3.drop(labels=idx)
        else:
            index_list.append(idx)
    return df3, index_list
