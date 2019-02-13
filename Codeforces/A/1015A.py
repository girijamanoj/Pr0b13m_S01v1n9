import sys
input=sys.stdin.readline
n,m=map(int,input().split())
e=[1]*(m+1)
for i in range(n):
    l,r=map(int,input().split())
    for j in range(l,r+1):
        e[j]=0
print(sum(e[1::]))
for i in range(1,m+1):
    if(e[i]==1):
        print(i,end=" ")
