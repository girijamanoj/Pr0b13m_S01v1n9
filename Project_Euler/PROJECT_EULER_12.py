

def count(n):
    result_set = set()
    if(n%2==0):
        k=n//2
        n=n+1
    else:
        k=(n+1)//2
    for i in range(1, 1+int(n**0.5)):
        if n % i == 0:
            result_set.add(n // i)
            result_set.add(i)
    result_set2 = set()

    for i in range(1, 1+int(k**0.5)):
        if k % i == 0:
            result_set2.add(k // i)
            result_set2.add(i)        
    return len(result_set)*len(result_set2)
def tri(d):
    return d*(d+1)//2

n=int(input())
for i in range(n):
    k=int(input())
    d=0
    while(count(d)<=k):
        
        d+=1
    print(tri(d))
    
