from math import gcd
n=int(input())
s=0
for i in range(2,n):
    k=n
    while k!=0:
        s+=k%i
        k=k//i
p=gcd(s,n-2)        
print(str(s//p)+"/"+str((n-2)//p))
