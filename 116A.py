n=int(input())
p=0
x=[]
for i in range(n):
    l=list(map(int,input().split()))
    p=p-l[0]
    p=p+l[1]
    x.append(p)
print(max(x))    
