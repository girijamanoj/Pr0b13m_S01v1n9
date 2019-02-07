import sys,math,string
input=sys.stdin.readline

L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split())
M=lambda : map(int,input().split())
d="RBG"
n=int(input())
s=list(input().strip())
i=0
c=0
if(n==1):
    print(0)
    print("".join(s))
else:
    while(i<n-2):
        if(s[i]==s[i+1]):
            c+=1
            if(s[i+2]==s[i]):
                f=list(d)
                f.remove(s[i])
                s[i+1]=f[0]
            else:
                f=list(d)
                f.remove(s[i+2])
                f.remove(s[i])
                s[i+1]=f[0]
            i+=1
        i+=1
    if(s[-2]==s[-1]):
        
        f=list(d)
        c+=1
        f.remove(s[-1])
        s[-1]=f[0]
    print(c)
    print("".join(s))
