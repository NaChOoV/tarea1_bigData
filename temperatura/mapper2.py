#!/usr/bin/python

# Format of each line is: 
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

pos = 0

for line in sys.stdin:
    data = line.strip().split(",")
    if len(data) == 3 or data[0] == "date":
	pos = data.index("smart_194_raw")	
	continue
    print "{0},{1}".format(data[pos], 1)

