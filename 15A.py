n,m=input().split()
n,m=int(n),int(m)
l=[]
count=0
for i in range(n):
    k=input().split()
    l.append(int(k[0])-(int(k[1])/2))
    l.append(int(k[0])+(int(k[1])/2))
l.sort()
for i in range(1,len(l)-1,2):
    if l[i+1]-l[i]>m:
        count+=2
    elif l[i+1]-l[i] == m:
        count+=1
print(count+2)        
