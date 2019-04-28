#!/usr/bin/python

import sys

failTotal = 0
oldKey = None

models = []


for line in sys.stdin:
    data_mapped = line.strip().split(",")
    if len(data_mapped) != 2:
        continue

    thisKey, thisFail = data_mapped

    if oldKey and oldKey != thisKey:
	models.append([oldKey,failTotal])
        #print oldKey, "\t", failTotal
        oldKey = thisKey;
        failTotal = 0

    oldKey = thisKey
    failTotal += int(thisFail)

if oldKey != None:
    models.append([oldKey,failTotal])
    #print oldKey,"\t", failTotal

# ordenamos de mayor a menor e imprimimos los 5 primeros
models.sort(key=lambda x: (x[1] * -1, x[0]))

for i in range(5):
    print models[i][0], models[i][1]


