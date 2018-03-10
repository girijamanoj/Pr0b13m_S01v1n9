n=int(input())
for i in range(n):
    n,k=map(int, input().split())
    s=list(input())
    l=0
    u=0
    for i in range(len(s)):
        if s[i].islower():
            l=l+1
        else:
            u=u+1
    if u<=k and l<=k:
        print("both")
    elif u<=k and l>k:
        print("chef")
    elif u>k and l<=k:
        print("brother")
    else :
        print("none")
    
    
