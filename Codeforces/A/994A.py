import sys
input=sys.stdin.readline
L=lambda : list(map(int,input().split()))
M=lambda : map(int,input().split())
n,m=M()
l=L()
k=L()
g=[]
for i in k:
    if i in l:
        g.append(l.index(i))
g.sort()
for i in g:
    print(l[i],end=" ")
