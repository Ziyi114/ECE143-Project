from math import radians, sin, cos, asin, sqrt
import pandas as pd


def Revenue(dis: float) -> float:
    """
    This function will return the revenue of taxi drivers given a specific distance
    :param dis: travel distance in this time slot
    :return: return a revenue number
    """
    Rev = 16 if dis <= 3 else 16 + (dis - 3) * 2.5
    return Rev


def calDistance(old_long, old_lat, new_long, new_lat):
    """
    This function will return the disctance between two locations
    given the longitude and latitude
    :param old_long: previous longitude
    :param old_lat: previous latitude
    :param new_long: current longitude
    :param new_lat: current latitude
    :return: distance between these two locations
    """
    lon1, lat1, lon2, lat2 = map(radians, [old_long, old_lat, new_long, new_lat])
    d_lon = lon2 - lon1
    d_lat = lat2 - lat1
    aa = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    c = 2 * asin(sqrt(aa))
    r = 6371
    return c * r


def get_averageRevenue(path1):
    """
    This function computes the revenue by calculating the distance
    :param path1: the path of taxi dataset
    :return: the average revenue of taxis in each time slot
    """
    dict_five = {}
    ave_rev = []
    for hour in range(24):
        for min in range(60):
            path = path1 + str(hour).zfill(2) + '//180401' + str(hour).zfill(2) + str(min).zfill(2) + '.txt'
            data = pd.read_csv(path, sep='|', header=None, encoding="ISO-8859-1")
            for row in data.itertuples():
                if row[1] in dict_five:  # check whether this Taxi ID is in dictionary
                    if row[4]:  # check whether the car is operating
                        if dict_five[row[1]][3]:  # check whether this taxi is operating in the last loop
                            dict_five[row[1]][0] += calDistance(dict_five[row[1]][1], dict_five[row[1]][2], row[11],
                                                                row[12])
                            dict_five[row[1]][1] = row[11]
                            dict_five[row[1]][2] = row[12]
                        else:  # update the running state in dictionary
                            dict_five[row[1]] = [0, row[11], row[12], 1]
                    else:
                        dict_five[row[1]][3] = 0
                else:  # if not, add this new taxi id set into dictionary
                    dict_five[row[1]] = [0, row[11], row[12], row[4]]
            moneySum = 0
            runningCarNum = 0
        for value in dict_five.values():
            if value[0] != 0:
                moneySum += Revenue(value[0])
                runningCarNum += 1
        ave_rev.append(round(moneySum / runningCarNum, 2))
    return ave_rev
