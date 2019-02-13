import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
print("EHAASRYD"[int(bool(sum(l)))::2])

    
