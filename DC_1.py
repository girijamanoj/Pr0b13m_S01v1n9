n=int(input())
a=1
b=1
s=2
if (n>2):
    while(n-2!=0):
        
        a,b=b,a+b
        s+=b
        n-=1
    print(s)    
else:
    if(n==1):
        print(1)
    else:
        print(2)
        
