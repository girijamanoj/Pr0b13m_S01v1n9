import sys,math
input=sys.stdin.readline
L=lambda : list(map(int,input().split().strip()))
M=lambda : map(int,input().split())
n=input().strip()
print(n+n[-1::-1])
