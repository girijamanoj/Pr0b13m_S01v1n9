def sum(n):
    s=0
    while(n!=0):
        s+=n%10
        n=n//10
    return s    
n=int(input())
for i in range(n):
    k=int(input())
    print(sum(2**k))
