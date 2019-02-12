import sys,math,string
input=sys.stdin.readline

L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split().strip())
M=lambda : map(int,input().split())
n=int(input())
l=L()
k=max(l)
print(k*n-sum(l))
