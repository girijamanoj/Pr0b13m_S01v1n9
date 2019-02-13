import math
def py(n):
    i=2
    k=n
    d=0
    a=[0]*(n+1)
    while(n!=1):
        if(i>math.sqrt(n) and d==0):
            a[k]=1
            break
        if(n%i==0):
           a[i]+=1
           d=1
           n/=i
        else:
            if(i==2):
                i+=1
            else:
                i+=2
    return a
n=int(input())

d=py(n)

x=max(d)
print (x)
f=math.ceil(math.log(x,2))
mul=0
p=1
for i in range(len(d)):
    if(d[i]>0):
        p*=i
        if(d[i]!=(2**f)):
            mul=1
if(p==n):
    print(p,0)
elif(x%2!=0):
    x=x+1
    print(p,f+1)
else:
    print(p,f+mul)
