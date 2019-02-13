import sys
input=sys.stdin.readline
n=input()
l=list(map(int,input().split()))
m=list(map(int,input().split()))
print("YNeos"[sum(l)<sum(m)::2])
