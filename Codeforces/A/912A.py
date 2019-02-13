n,m=map(int,input().split())
k=list(map(int,input().split()))
yellow=(k[0]*2)+k[1]
blue=k[2]*3+k[1]
s=0
if yellow>n:
    s=s+(yellow-n)
if blue>m:
    s=s+(blue-m)
print(s)

    
    
