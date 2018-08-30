l=[]
for i in range(5):
    a=input().split()
    l.append(a)
d=0    
for i in range(5):
    for j in range(5):
        if l[i][j]=='1':
            p=i
            q=j
            d=1
            break
    if d==1:
        break
print(abs(3-(p+1))+abs(3-(q+1)))  
