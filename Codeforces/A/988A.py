import sys
input=sys.stdin.readline
L=lambda : list(map(int,input().split()))
M=lambda : map(int,input().split())
n,k=M()
l=L()
s=list(set(l))
if(len(s)<k):
    print("NO")
else:
    g=[]
    print("YES")
    for i in range(k):
        g.append(l.index(s[i])+1)
    g.sort()
    print(*g)
