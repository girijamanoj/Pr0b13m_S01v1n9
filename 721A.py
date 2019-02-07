import sys,math,string
input=sys.stdin.readline

L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split("W"))
M=lambda : map(int,input().split())

n=int(input())
l=input()
g=[]
c=0
for i in l:
    if(i=="B"):
        c+=1
    else:
        if(c>0):
            g.append(c)
        c=0
if(l[-1]=="B"):
    g.append(c)
print(len(g))
print(*g)
