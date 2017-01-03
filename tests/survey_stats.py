import pandas

import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier
import numpy as np

df = pandas.read_csv('../docs/survey.csv')

def isnan(x):
    return x != x

lastID = 0
def coding(x, code):
    global lastID
    if isinstance(x,str):
        if not x in code:
            lastID += 1
            code[x] = lastID

        return code[x]

    if isnan(x):
        return 0

    return x


# replace values
code = {}
for column in df:
    lastID = 0
    df[column].map(lambda x: coding(x, code))

results = list()
for row in df.values:
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
                results.append(row[1:20].tolist() + [floor])
    else:
        results.append(row[1:20].tolist() + [currentFloor])

vectCoding = np.vectorize(coding)
results = vectCoding(np.array(results), code)
forest = ExtraTreesClassifier(n_estimators = 100)
X = results[0::,1:-1]
y = results[0::,-1]

forest = forest.fit(X,y)

importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in range(X.shape[1]):
    print("%d. feature '%s' (%f)" % (f + 1, df.columns[indices[f]], importances[indices[f]]))

# Plot the feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(range(X.shape[1]), importances[indices],
       color="r", yerr=std[indices], align="center")
plt.xticks(range(X.shape[1]), indices)
plt.xlim([-1, X.shape[1]])
plt.show()
