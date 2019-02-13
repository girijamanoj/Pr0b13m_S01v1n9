import sys,math
input=sys.stdin.readline

L=lambda : list(map(int,input().split().strip()))
M=lambda : map(int,input().split())
n,q=M()
s=["o"]+list(input().strip())
for i in range(q):
    l,r,c1,c2=input().split()
    l,r=int(l),int(r)
    for j in range(l,r+1):
        if(s[j]==c1):
            s[j]=c2
s=s[1::]
print(*s,sep="")
