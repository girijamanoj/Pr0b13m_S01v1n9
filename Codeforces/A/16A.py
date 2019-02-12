n,m=input().split()
n,m=int(n),int(m)
d=0
h=0
g=[]
for i in range(n):
    l=input()
    p=set(l[:])
    g.append(p)
    if len(p)!=1:
        print("NO")
        d=1
        break
if d==0:
    for i in range(len(g)-1):
        if g[i]==g[i+1]:
            print("NO")
            h=1
            break
    if h==0:
        print("YES")
