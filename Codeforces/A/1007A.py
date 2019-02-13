from collections import*
n=int(input())
l=max(Counter(map(int,input().split())).values())
print(n-l)
