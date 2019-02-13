import sys,math
input=sys.stdin.readline

L=lambda : list(map(int,input().split().strip()))
M=lambda : map(int,input().split())
n=int(input())
s=input()
if(s.count("SF")>s.count("FS")):
    print("YES")
else:
    print("NO")
