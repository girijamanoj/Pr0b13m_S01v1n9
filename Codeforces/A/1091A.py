import sys
input=sys.stdin.readline
print=sys.stdout.write
y,b,r=map(int,input().split())
print(str(3*min(y+1,b,r-1)))
