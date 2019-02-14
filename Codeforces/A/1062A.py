n=int(input())
l=list(map(int,input().split()))
l.append(l[-1]+1)
c=0
d=[]
if(n>1):
    for i in range(1,n):
        
        if(l[i]-l[i-1]==1):
            if(l[i-1]==1):
                c+=1
            elif(l[i]==1000):
                c+=1
            c+=1
        else:
            d.append(c-1)            
            c=0
    if(c<=0):
        c=1
    d.append(c-1)
    print(max(d))
else:
    print(0)
