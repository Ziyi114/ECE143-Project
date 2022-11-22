def ifInAirportField(longi, lati):
    """
    this function is to check whether the taxi is in the airport waiting field

    :param longi: float, longtitude
    :param lati: float, latitude
    :rtype: bool
    """
    assert isinstance(longi, float)
    assert isinstance(lati, float)
    if 121.8164 <= longi < 121.8195 and 31.1157 <= lati <= 31.1192:
        return True  # the taxi is in the area
    return False  # not in the area
