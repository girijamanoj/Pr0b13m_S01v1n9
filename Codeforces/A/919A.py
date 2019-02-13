n,m=map(int,(input().split()))
l=[]
for i in range(n):
    p,q=map(int,(input().split()))
    l.append(p/q)
print(min(l)*m)
