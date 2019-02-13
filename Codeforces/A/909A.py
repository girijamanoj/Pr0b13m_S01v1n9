k=input().split()
a=k[0][0]
for i in range(1,len(k[0])):
    if k[0][i]<k[1][0]:
        a+=k[0][i]
    else:
        break
print(a+k[1][0])    
        
    
    
