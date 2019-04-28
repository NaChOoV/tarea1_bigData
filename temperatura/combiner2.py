#!/usr/bin/python

import sys

total_disk = 0
oldKey = None



for line in sys.stdin:
    data_mapped = line.strip().split(",")
    if len(data_mapped) != 2:
        continue

    thisKey, disk = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, ",", total_disk
        oldKey = thisKey;
        total_disk = 0

    oldKey = thisKey
    total_disk += int(disk)

if oldKey != None:
    print oldKey,",", total_disk

