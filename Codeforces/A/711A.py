import sys,math,string
input=sys.stdin.readline

L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split())
M=lambda : map(int,input().split())
n=int(input())
a=0
b=0
for i in range(n):
    q,w=M()
    a+=int(q>w)
    b+=int(w>q)
if(a==b):
    print("Friendship is magic!^^")
elif(a>b):
    print("Mishka")
else:
    print("Chris")
