import numpy as np

def readFileToArray(fileName):
    data = []
    with open(fileName, 'r') as file:
        headLine = file.readline()
        if (len(headLine.rstrip()) > 1):
            data.append(headLine.rstrip().split(','))
            for line in file:
                data.append(line.rstrip().split(','))
            floatData = [[int(j) for j in i] for i in data]
        else:
            data.append(headLine.rstrip())
            for line in file:
                data.append(line.rstrip())
            floatData = [int(i) for i in data]
    return np.asarray(floatData)


def convertStringListToFloat(lst):
    newList = []
    for line in lst:
        parts = []
        for part in line:
            parts.append(float(part))
        newList.append(parts)
    return newList
