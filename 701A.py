import sys,math,string
input=sys.stdin.readline

L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split())
M=lambda : map(int,input().split())
a,b=M()
print(min(a,b)//2,max(a-min(a,b),b-min(a,b))//2)
