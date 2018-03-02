from math import gcd
def lcm(x,y):
    return (x*y//gcd(x,y))
k=int(input())
l=int(input())
m=int(input())
n=int(input())
p=int(input())
j=[]
for i in range(1,p+1):
    if i%k==0 or i%l==0 or i%m==0 or i%n==0:
        j.append(1)
    else:
        j.append(0)
print(j.count(1))
        
    
