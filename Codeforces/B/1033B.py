import math
def prime(n):
    i=2
    while(i<=math.sqrt(n)):
        if(n%i==0):
            return False
        else:
            if(i==2):
                i+=1
            else:
                i+=2
    return True

n=int(input())
for i in range(n):
    n,m=map(int,input().split())
    m+=1
    if(n==m and prime(2*m-1)):
        print("YES")
    else:
        print("NO")
