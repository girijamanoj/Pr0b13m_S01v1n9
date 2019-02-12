#!/bin/python3

import math


t = int(input().strip())


for a0 in range(t):
    n = int(input().strip())
    a=0
    b=2
    count=0
    while 4*b+a<n:
        
        c=4*b+a
        
        a=b
        b=c
        count=count+a
        
    print(count+b)
