#!/usr/bin/python3
import sys
for line in sys.stdin:
    linelist=line.split()
    for word in linelist:
        print(word,1)
