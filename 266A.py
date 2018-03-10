n=int(input())
l=input()
c=0
for i in range(n-1):
    if l[i]+l[i+1]=="RR" or l[i]+l[i+1]=="BB" or l[i]+l[i+1]=="GG":
        c+=1
print(c)        
        
