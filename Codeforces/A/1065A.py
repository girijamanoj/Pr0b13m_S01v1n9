import sys
input=sys.stdin.readline

n=int(input())
for i in range(n):
    s,a,b,c=map(int,input().split())
    k=s//c
    f=(k//a)*b
    print(k+f)
