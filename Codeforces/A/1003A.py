n=int(input())
l=list(map(int,input().split()))
l.sort()
s=set(l)
m=0
for i in s:
   if(m<l.count(i)):
       m=l.count(i)
print(m)
