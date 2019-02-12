import sys,math,string
input=sys.stdin.readline

L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split())
M=lambda : map(int,input().split())
n,c=M()
l=L()
s=0
for i in range(n-1,0,-1):
    if(l[i]-l[i-1] > c ):
        print(s+1)
        exit()
    else:
        s+=1
print(s+1)
