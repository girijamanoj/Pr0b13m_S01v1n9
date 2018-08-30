#!/bin/python3

import math


t = int(input())
for a0 in range(t):
    n = int(input())
    
    i=2
    
    g=0
    while i<=math.sqrt(n):
        
        if n%i==0:
            n=n//i
            g=i
            i=1
        i=i+1
    print(max(g,n))
                
         
