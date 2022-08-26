#!python3

import sys 
import datetime 

argv = sys.argv 
ignore = True 
onlyCashLoan = True 
cmpDate = datetime.datetime.now() - datetime.timedelta(minutes=15)

if len(argv) > 1:
    for av in argv:
        if av.startswith("2022"):
            cmpDate = datetime.datetime.strptime(argv[1], "%Y-%m-%d %H:%M:%S")
        elif av.startswith("n"):
            onlyCashLoan = False


for line in sys.stdin:
    if line.startswith("2022"):
        it = line[0:19]
        date = datetime.datetime.strptime(it, "%Y-%m-%d %H:%M:%S")
        if cmpDate > date:
            continue 
       
        if onlyCashLoan and line.count("CASH_LOAN") == 0:
            ignore = True
            continue

        ignore = False
    line = line.replace("\n", "")
    if not ignore:
        print(line)
