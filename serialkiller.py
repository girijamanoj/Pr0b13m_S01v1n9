n=int(input())
k=int(input())
a=[]
for i in range(0,n):
    a.append(i+1)
i=k-1
while(len(a)!=1):
    a.remove(a[i])
    print(a)
    if len(a)!=0:
        i=(i+k-1)%len(a)
print(a[0])    
    
    
    

    
