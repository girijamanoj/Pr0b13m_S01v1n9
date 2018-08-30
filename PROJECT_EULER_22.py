def sum(s):
    c=0
    for i in s:
        c+=(ord(i)-64)
    return c    
n=int(input())
k=[]
for i in range(n):
    k.append(input())
k=sorted(k)
t=int(input())
for i in range(t):
    p=input()
    y=k.index(p)+1
    y=y*sum(p)
    print(y)
    
