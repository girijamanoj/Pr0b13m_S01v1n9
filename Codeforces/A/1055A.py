n,s=map(int,input().split())
l=list(map(int,input().split()))
d=list(map(int,input().split()))
x=0
if(l[0]):
    if(l[s-1]==1):
        x=1
        print("YES")
    else:
        for i in range(s-1,n):
            if((l[i]==1 and d[i]==1) and d[s-1]==1):
                print("YES")
                x=1
                break
        if(x==0):
            print("NO")
else:
    print("NO")
                
                
