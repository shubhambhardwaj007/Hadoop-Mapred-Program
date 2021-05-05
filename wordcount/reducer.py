#!/usr/bin/python3
import sys
(last_key,count)=(None,0)
for line in sys.stdin:
    (key,value)=line.strip().split()
    if last_key!=key:
        print(last_key,count)
        (last_key,count)=(key,int(value))
    else:
        (last_key,count)=(key,count+int(value))
      

