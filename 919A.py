a,b=map(int,input().split())
#print(a,b)
l=[]
for i in range(a):
    m,n=map(int,input().split())
    l.append((m/n)*b)
print(min(l))
    
