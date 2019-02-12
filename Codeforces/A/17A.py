n,m=map(int,input().split()) #taking the input
l=[]
k,count = 0,0
for i in range(2,n+1):
    d,e = 0,0
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
    print("YENOS"[::len(l)<m or count<m])
