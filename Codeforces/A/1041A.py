import sys
import math
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
l.sort()
print(l[-1]-(l[0]+n-1))
