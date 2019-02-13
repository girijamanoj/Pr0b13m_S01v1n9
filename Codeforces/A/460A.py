d n,m=list(map(int,input().split()))
c=n
d=0
while c!=0:
    d+=1
    c-=1
    if d%m==0:
        c+=1
print(d)    
