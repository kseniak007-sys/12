#!/usr/bin/python3
import sys

b = sys.stdin.readlines()     
b.sort(reverse=True)
for line in b:                
    print(line, end='')


