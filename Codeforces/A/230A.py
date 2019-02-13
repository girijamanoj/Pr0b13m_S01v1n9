s,n=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
l.sort()
for i,j in l:
    s=(s+j)*(s>i)
print('YNEOS'[(s<1)::2])    
    
    
