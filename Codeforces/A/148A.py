k=int(input());l=int(input());m=int(input());n=int(input());p=int(input())
j=0
for i in range(1,p+1):
    if i%k==0 or i%l==0 or i%m==0 or i%n==0:
        j+=1
print(j)
        
    
