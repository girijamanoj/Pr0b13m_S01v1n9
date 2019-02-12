l=[0]
i=19
k=1
def s10(n):
    i = 0
    while(n>0):
        i+=n%10
        n//=10
    return i==10
while(len(l)<=1000):
    
    if(k%10==0):
        k+=k//10
        if(not(s10(19+(k-1)*9))):
            k+=1 
    else:
        k+=1
        if(not(s10(19+(k-1)*9))):
            k+=1 
    l.append(19+(k-1)*9)
print(l)
