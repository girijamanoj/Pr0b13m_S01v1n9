import sys
input=sys.stdin.readline
n=int(input())
if(n%3==2):
    print(1,2,n-3)
else:
    print(1,1,n-2)
