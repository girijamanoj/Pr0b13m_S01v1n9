import sys,math,string
input=sys.stdin.readline

L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split().strip())
M=lambda : map(int,input().split())
a,b,c=M()
k=(a+b+c)//3
print(abs(k-a)+abs(k-b)+abs(k-c))
