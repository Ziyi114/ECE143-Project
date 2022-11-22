import pandas as pd
import ifInAirportField


def get_CarInLotPerSlots(location, index_list):
    """
    this function is to calculate the number of waiting cars in the parking lot for each time slot. The time slot is
    every 5 minutes in a day.

    :param location: str
    :param index_list: list
    :rtype: pd.DataFrame
    """
    assert isinstance(location, str)
    assert isinstance(index_list, list)
    CarNumPerMin = []
    for hour in range(24):
        for quarter in range(12):
            for i in range(5):
                min = quarter * 5 + i
                path = location + str(hour).zfill(2) + '//180401' + str(hour).zfill(2) + str(min).zfill(2) + '.txt'
                data = pd.read_csv(path, sep='|', header=None, encoding="ISO-8859-1")
                temp_list = []
                for row in data.itertuples():
                    if ifInAirportField.ifInAirportField(row[11], row[12]):
                        if row[1] not in temp_list and row[1] in index_list:
                            temp_list.append(row[1])
            CarNumPerMin.append([str(hour).zfill(2) + str(min).zfill(2), len(temp_list)])
    carNumTable1 = pd.DataFrame(CarNumPerMin)
    return carNumTable1
