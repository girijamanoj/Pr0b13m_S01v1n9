n=int(input())
l=list(map(int,input().split()))
l.sort()
l.reverse() #Reverses the list
x=sum(l)
count=0
p=0
for i in range(len(l)):
    p+=l[i]
    count+=1
    if p>x-p:
        print(count)
        break
        
