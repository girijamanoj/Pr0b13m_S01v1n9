o,n,e=0,0,0
for i in range(int(input())):
    k=list(map(int,input().split()))
    o+=k[0]
    n+=k[1]
    e+=k[2]
if o==0 and n==0 and e==0:
    print("YES")
else:
    print("NO")
    
