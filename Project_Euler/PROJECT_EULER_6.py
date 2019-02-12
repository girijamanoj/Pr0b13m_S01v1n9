#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print((((3*n)+2)*((n**2)-1)*n)//12)
