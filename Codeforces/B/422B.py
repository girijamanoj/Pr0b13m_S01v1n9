n,m=map(int,input().split())
s=list(input())
t=list(input())
m=[]
min=10000
for i in range(len(t)-len(s)+1):
    c=0
    l=[0]*n
    for j in range(len(s)):
        if(s[j]!=t[i+j]):
            c+=1
            l[j]=1
    if(min>c):
        min=c
        m=l[::]
        
print(min)
for i in range(n):
    if (m[i]==1):
        print(i+1,end=" ")
            
