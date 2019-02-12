#!/bin/python3

import sys
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
def lcm(x,y):
    return (x*y)//gcd(x,y)
t = int(input())
for a0 in range(t):
    n = int(input())
    g=1
    for i in range(1,n+1):
        g=lcm(g,i)
        
    print(g)    
