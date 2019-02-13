import sys,math
input=sys.stdin.readline

L=lambda : list(map(int,input().split()))
M=lambda : map(int,input().split())

l=L()
if(l[2]<=l[1]):
    print(l[2])
elif(l[2]>l[0]):
    print(l[1]-(l[2]%l[0]))
else:
    print(l[1])
