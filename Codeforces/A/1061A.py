import sys
input=sys.stdin.readline
n,s=map(int,input().split())
print(s//n+int(bool(s%n)))
