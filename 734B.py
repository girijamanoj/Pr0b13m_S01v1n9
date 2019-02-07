import sys,math,string
input=sys.stdin.readline

L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split().strip())
M=lambda : map(int,input().split())
a,b,c,d=M()
print(min(a,c,d)*256+min(a-min(a,c,d),b)*32)
