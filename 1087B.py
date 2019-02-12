n,k=map(int,input().split())
i=k-1
d=0
while(i>=1):
    if(n%i==0):
        f=n//i
        d=1
        break
    i-=1
if(d==0):
    i=1
    f=n

ans=(f*k)+i
print(ans)

