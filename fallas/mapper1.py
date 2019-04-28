#!/usr/bin/python



import sys

for line in sys.stdin:
    data = line.strip().split(",")
    if len(data) == 3 or data[0] == "date":
	continue
    print "{0},{1}".format(data[2], data[4])

