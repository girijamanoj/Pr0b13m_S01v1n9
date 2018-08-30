#!/bin/python3

import sys
def sig(p):
    return(p*(p+1)//2)
  

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x=(n-1)//3
    y=(n-1)//5
    z=(n-1)//15
    print((3*sig(x))+(5*sig(y))-(15*sig(z)))
