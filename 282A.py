n=int(input())
c=0
for i in range(n):
    k=input()
    if k[0]=='+' or k[1]=='+':
        c+=1
    else:
        c-=1
print(c)        
