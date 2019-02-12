#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    c=0
    for i in range(len(num)-k+1):
        p=num[i:i+k]
        
        h=1
        
        for j in range(0,k):
            
            h=h*int(p[j])
            
        if h>=c:
            c=h
    print(c)            
