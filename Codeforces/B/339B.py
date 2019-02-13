n,k=map(int,input().split())
l=list(map(int,input().split()))
p=1
c=0
for i in range(k):
    if l[i]>p:
        c+=l[i]-p
        p=l[i]
    elif l[i]<p:
        c+=((n-p)+l[i])
        p=l[i]
print(c)
