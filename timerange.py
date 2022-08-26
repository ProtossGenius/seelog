#!python3

import sys 
import datetime 

argv = sys.argv 
ignore = True 

if argv.__len__ == 1:
   print("need date") 
   exit(2)

for line in sys.stdin:
    if line.startswith("2022"):
        it = line[0:19]
        date = datetime.datetime.strptime(it, "%Y-%m-%d %H:%M:%S")
        t = datetime.datetime.strptime(argv[1], "%Y-%m-%d %H:%M:%S")
        if t > date:
            continue 
       
        if line.count("CASH_LOAN") == 0:
            ignore = True
            continue

        ignore = False

    if not ignore:
        print(line)
