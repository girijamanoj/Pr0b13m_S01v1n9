l=[]
g=[] #empty list
for i in range(3):
    l.append(input())
for i in range(3):
    s=''
    for j in range(2,-1,-1):
        s=s+l[i][j]
    g.append(s)
g.reverse()    
if "".join(l)=="".join(g):
    print("YES")
else:
    print("NO")
