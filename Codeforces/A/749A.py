import sys,math,string
input=sys.stdin.readline

L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split().strip())
M=lambda : map(int,input().split())
n=int(input())
k=n//2
l=[2]*(k-n%2)
l+=[3]*int(bool(n%2))

print(len(l))
print(*l)
