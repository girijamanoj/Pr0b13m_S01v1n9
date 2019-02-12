n,m=input().split()
n,m=int(n),int(m)
k=list(map(int,input().split()))
k.sort()
l=[]
for i in range(len(k)-n+1):
    l.append(k[i+n-1]-k[i])
print(min(l))
