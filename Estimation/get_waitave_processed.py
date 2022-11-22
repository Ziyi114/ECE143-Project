from statistics import stdev,mean


def get_waitave_processed(waitave):
    """
    This function processes the outliers of average waittime
    :param waitave: average wait-time
    :return: outliers processed average waittime
    """
    upper = mean(waitave) + 1.5 * stdev(waitave)
    lower = mean(waitave) - 1.5 * stdev(waitave)
    waitave_process = []
    for i in range(len(waitave)):
        if lower < waitave[i] < upper:
            waitave_process.append(waitave[i])
        else:
            waitave_process.append(0)
    for i in range(len(waitave)):
        if waitave_process[i] == 0:
            tmp = []
            k = 0
            for j in range(1, 4):
                while waitave_process[(i + j + k) % len(waitave_process)] == 0:
                    k += 1
                tmp.append(waitave_process[(i + j + k) % len(waitave_process)])
            for j in range(1, 4):
                while waitave_process[(i - j - k) % len(waitave_process)] == 0:
                    k += 1
                tmp.append(waitave_process[(i - j - k) % len(waitave_process)])
            waitave_process[i] = sum(tmp) / len(tmp)
    return waitave_process
