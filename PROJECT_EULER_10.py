#!/bin/python3

import sys
def primesgen(n):
    primes=dict()
    for i in range(2,n+1):primes[i]=True
    
    for i in primes:
        multiples=range(i,n+1,i)
        if(primes[i]==True):
            for j in multiples[1:]:
                primes[j]=False
    s=0
    l=[0,0]
    for i in primes:
        if(primes[i]==True):
            s=s+i
        l.append(s)        
    return l


t=int(input())
h=[]
for i in range(t):
    
    n=int(input())
    h.append(n)
l=primesgen(max(h))

for i in range(len(h)):
    print(l[h[i]])
