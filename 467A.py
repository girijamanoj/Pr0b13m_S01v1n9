c=0
for i in range(int(input())):
    k=list(map(int,input().split()))
    if k[1]-k[0]>=2:
        c+=1
print(c)
    
