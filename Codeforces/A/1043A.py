import sys
import math
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
s=sum(l)
print(max(max(l),2*s//n+1))
