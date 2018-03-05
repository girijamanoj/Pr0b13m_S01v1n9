n,m=input().split()
n,m=int(n),int(m)
l=[]
k=0
count=0
for i in range(2,n+1):
    d=0
    e=0
    for j in range(2,i):
        if i%j==0:
            d=1
            break
    if d==0:
        l.append(i)
        k=k+1
        e=1
    if len(l)>=3 and e==1:
        for b in range(k-2):
            if l[k-1]==l[b]+l[b+1]+1:
                count+=1
                if count>=m:
                    break
    if count>=m:
                    break
        
           
if len(l)<m or count<m:
    print("NO")
else:
    print("YES")
