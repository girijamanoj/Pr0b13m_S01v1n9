n,m=input().split()
n,m=int(n),(int(m)-1)
l=list(map(int,input().split()))
count=0
for i in range(len(l)):
    if l[i]>=l[m] and l[i]>0:
        count+=1
        
print(count)
