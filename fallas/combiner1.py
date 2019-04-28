import sys

failTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split(",")
    if len(data_mapped) != 2:
        continue

    thisKey, thisFail = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, ",", failTotal
        oldKey = thisKey;
        failTotal = 0

    oldKey = thisKey
    failTotal += float(thisFail)

if oldKey != None:
    print oldKey, ",", failTotal

