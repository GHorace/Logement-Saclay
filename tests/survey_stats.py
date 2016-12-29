import pandas

import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.cluster import KMeans

df = pandas.read_csv('../docs/survey.csv')

def isnan(x):
    return x != x

results = list()
for row in df.values:
    noteCommunity = row[4]
    noteParty = row[5]
    noteWork = row[6]

    i = 21
    while isnan(row[i]):
        i += 1
    currentFloor = str(i - 21) + str(row[i])

    if i == 26: #no floor given
        continue

    satisfied = row[26] == 'Oui'
    if not satisfied:
        desiredFloors = list()
        for i in range(27, 31):
            if not isnan(row[i]):
                floor = str(i - 27) + str(row[i])
                desiredFloors.append(floor)
                results.append((noteCommunity, noteParty, noteWork, floor))
    else:
        results.append((noteCommunity, noteParty, noteWork, currentFloor))

print(results)