import sys,math,string
input=sys.stdin.readline

L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split().strip())
M=lambda : map(int,input().split())
n,r=M()
for i in range(1,10):
    if((i*n)%10==0):
        print(i)
        break
    elif((n*i)%10==r):
        print(i)
        break
