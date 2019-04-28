#!/usr/bin/python

import sys

pos = 0

for line in sys.stdin:
    data = line.strip().split(",")
    if data[0] == "date":	
	    continue
    if len(data) == 105:
        pos = 60
    elif len(data) == 109:
        pos = 64
    elif len(data) == 129:
        pos = 76
    else:
        continue

    if len(data[pos]) == 2:
        print "0{0},{1}".format(data[pos], 1)
    else:
        print "{0},{1}".format(data[pos], 1)

