import sys,math
input=sys.stdin.readline
L=lambda : list(map(int,input().split()))
M=lambda : map(int,input().split())
n=int(input())
l=L()
b=0
c=0
for i in l:
    if(i>=0):
        b+=i
    else:
        c+=i
print(b-c)
