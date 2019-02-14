import sys
input=sys.stdin.readline
n,k=map(int,input().split())
s=list(input())
l=set(s[:n:])
if(len(l)<k):
    print(0)
else:
    g=[]
    for i in l:
        g.append(s.count(i))
    g.sort()
    print(k*g[-k])
