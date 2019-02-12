k=list(map(int,input().split(" ")))
if (k[0]%k[2]==0):
    p=k[0]//k[2]
elif (k[0]%k[2]!=0):
    p=(k[0]//k[2])+1
if (k[1]%k[2]==0):
    q=k[1]//k[2]
elif (k[1]%k[2]!=0):
    q=(k[1]//k[2])+1    
print(p*q)
