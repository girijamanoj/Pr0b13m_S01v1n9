n,m=input().split() #taking input n and m at a time.
n,m=int(n),int(m)
l=[]

f=0
t=0
for i in range(n):
    l.append(input())
for i in range(n):
    if l[i].count('*')!=0:
        u=i
        break
for i in range(n-1,-1,-1):
    if l[i].count('*')!=0:
        d=i
        break
for i in range(m):
    for j in range(n):
        
        if l[j][i]=='*' and f==0:
            left=i
            f=1
            break
    if f==1:
        break
for i in range(m-1,-1,-1):
    for j in range(n):
        
        if l[j][i]=='*' and t==0:
            right=i
            t=1
            break
    if t==1:
        break
   
for i in range(u,d+1):
    p=[]
    for j in range(left,right+1):
        p.append(l[i][j])
    print(''.join(p))    
     
