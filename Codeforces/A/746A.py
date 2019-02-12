import sys,math,string
input=sys.stdin.readline

L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split().strip())
M=lambda : map(int,input().split())
print(min(int(input()),int(input())//2,int(input())//4)*7)

