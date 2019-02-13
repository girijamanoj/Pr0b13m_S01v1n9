import sys,math
input=sys.stdin.readline

L=lambda : list(map(int,input().split()))
M=lambda : map(int,input().split())

n,k=M()
if((n//k)%2==1):
    print("YES")
else:
    print("NO")
    
