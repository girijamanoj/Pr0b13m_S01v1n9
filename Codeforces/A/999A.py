import sys
input=sys.stdin.readline
n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if(l[i]<=k):
        c+=1
    else:
        break
for i in range(n-1,-1,-1):
    if(l[i]<=k):
        c+=1
    else:
        break
print(min(n,c))
