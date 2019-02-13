k=int(input())
i=1
for i in range(1,k):
    p=(i*(i+1)*(i+2))//6
    if p>k:
        i=i-1
        break
print(i)
    
