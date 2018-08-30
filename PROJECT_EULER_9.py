#!/bin/python3

import sys


t = int(input().strip())


for a0 in range(t):
    product=-1
    d=0
    g = int(input().strip())
    for a in range(1,g//3):
        b=(g*g-2*a*g)//(2*g-2*a)
        c=g-a-b
        if c*c==(a*a+b*b):
            d=(a*b*c)
            
            if d>=product:
                product=d
    print(product)
            
    
