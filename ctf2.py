import re

a=[]
l=[]
while True:
    i= re.sub(' +',' ',input())
    if (i=='b'):
        break;
    k=re.split("\D+",i)
    while '' in k:
       k.remove('')
    l=[int(x) for x in k]
    
    a= a+l

print(sum(a))
