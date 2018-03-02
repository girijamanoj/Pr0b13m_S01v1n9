n,m=map(int,input().split())
k=list(map(int,input().split()))
c=1
d=0
for i in range(n-1):
    c+=k[i]
    if c==m:
        d=1
        print("YES")
        break
    elif c>m:
        d=1
        print("NO")
        break
if d==0:
    print("NO")
