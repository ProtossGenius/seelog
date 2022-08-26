#!python3

import sys 
import datetime 

argv = sys.argv 
ignore = True 

cmpDate = datetime.datetime.now() - datetime.timedelta(minutes=15)

if argv.__len__ > 1:
    cmpDate = datetime.datetime.strptime(argv[1], "%Y-%m-%d %H:%M:%S")


for line in sys.stdin:
    if line.startswith("2022"):
        it = line[0:19]
        date = datetime.datetime.strptime(it, "%Y-%m-%d %H:%M:%S")
        if cmpDate > date:
            continue 
       
        if line.count("CASH_LOAN") == 0:
            ignore = True
            continue

        ignore = False

    if not ignore:
        print(line)
