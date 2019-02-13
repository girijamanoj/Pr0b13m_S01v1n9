import sys
input=sys.stdin.readline
L=lambda : list(map(int,input().split()))
M=lambda : map(int,input().split())
n=int(input())
l=L()
s=list(set(l))
g=[]
for i in range(len(s)):
    g.append(n-1-l[::-1].index(s[i]))
g.sort()
print(len(s))
for i in range(len(g)):
    print(l[g[i]],end=" ")
