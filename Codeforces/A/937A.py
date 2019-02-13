import sys,math
input=sys.stdin.readline
L=lambda : list(map(int,input().split()))
M=lambda : map(int,input().split())
n=int(input())
l=L()
l=list(set(l))
print(len(l)-l.count(0))
