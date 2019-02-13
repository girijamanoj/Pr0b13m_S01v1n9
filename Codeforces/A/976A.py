import sys
input=sys.stdin.readline
L=lambda : list(map(int,input().split()))
M=lambda : map(int,input().split())
n=int(input())
s=input()
if(s.count("1")>0):
    print("1"+"0"*(s.count("0")))
else:
    print("0")
