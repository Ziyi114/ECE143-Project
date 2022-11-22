import pandas as pd


def downtownArea(longi, lati):
    """
    This function will return a bool value whether this location is in a specific area
    :param longi: longitude of downtownarea
    :param lati: latitude of downtownarea
    :return: True if the lacation is in the downtoenarea, else False
    """
    if 121.3814 <= longi < 121.6258 and 31.120 <= lati <= 31.346:
        return True
    return False


def get_runningPortions(path1):
    """
    This function will out put the running portion of all taxis in an area
    :param path1: the path of data need to be load
    :return: the running portion of all taxis in every 5-min time slot
    """
    dict_Five = {}
    running_portions = []
    for hour in range(24):
        for quarter in range(12):
            for i in range(5):
                min = quarter * 5 + i
                path = path1 + str(hour).zfill(2) + '//180401' + str(hour).zfill(2) + str(min).zfill(2) + '.txt'
                data = pd.read_csv(path, sep='|', header=None, encoding="ISO-8859-1")
                for row in data.itertuples():
                    if downtownArea(row[11], row[12]):
                        if row[1] in dict_Five:  # whether in the dictionary
                            dict_Five[row[1]][-1] = row[4]
                        else:  # add new record
                            dict_Five[row[1]] = [0, row[11], row[12], row[4]]
            runningNum = 0
            totalNum = 0

            for value in dict_Five.values():
                if value[-1] == 0:
                    runningNum += 1
                totalNum += 1
            running_portions.append(runningNum / totalNum)
    return running_portions
