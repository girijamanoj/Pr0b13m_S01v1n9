from sys import stdin, stdout 
n=int(stdin.readline())
l=list(map(int,stdin.readline().split()))
g=l[::]
g.sort()
k=sum(l)
p=k-2*g[-1]


r=sum(g[:n:])
d=r-2*g[-2]

f=0
if(d==g[-1]):
    f=1
m=l.count(p)
if(p==g[-1]):
    t=m-1+f
    
else:
    t=m+f
print(t)
if(t!=0):
    for i in range(n):
        if(l[i]==p or (f==1 and l[i]==g[-1])):
            h=str(i+1)+" "
            stdout.write(h)
