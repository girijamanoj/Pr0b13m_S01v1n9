import sys
input=sys.stdin.readline
L=lambda : list(map(int,input().split()))
M=lambda : map(int,input().split())
n=int(input())
l=L()
l.sort()
if(n%2==0):
    n=(n//2-1)
else:
    n=n//2
print(l[n])
