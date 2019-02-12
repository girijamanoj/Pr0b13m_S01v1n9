while 1:
       l.append(input())
except:
  exit(0)
print(l)
d=0
for i in l:
    if i[0]=='+':
        d+=1
    elif i[0]=='-':
        d-=1
    else:
        k=len((i.split(':'))[1])
        s=s+(k*d)
print(s)        
