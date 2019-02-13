import math

def prime(n):
    i=2
    while(i<=math.sqrt(n)):
        if(n%i==0):
            return i
        else:
            if(i==2):
                i+=1
            else:
                i+=2
    return n
n=int(input())
r=0
while(n!=0):
    d=prime(n)
    if(d==n):
        r+=1
        break
    else:
        if(n%2==0):
            r=r+n//2
            break
        else:           
            n-=d
            r+=1
print(r)
