'''There are N people standing in a circle. A serial killer who wants to kill every K'th person in the circle except the last one
in the circle. Joseph who is very good at math want to survive in this process but wants your help to survive,Help him by finding 
the position that he have to stand'''


n=int(input())
k=int(input())
a=[]
for i in range(0,n):
    a.append(i+1)
i=k-1
while(len(a)!=1):
    a.remove(a[i])
    print(a)
    if len(a)!=0:
        i=(i+k-1)%len(a)
print(a[0])    
    
    
    

    
