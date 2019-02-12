n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
c=0
for i in range(1,n,2):
    c+=l[i]-l[i-1]
print(c)
