import sys
input=sys.stdin.readline
L=lambda : list(map(int,input().split()))
M=lambda : map(int,input().split())
n=int(input())
d={}
d["purple"]="Power"
d["green"]="Time"
d["blue"]="Space"
d["orange"]="Soul"
d["red"]="Reality"
d["yellow"]="Mind"
l=["Power","Time","Space","Soul","Reality","Mind"]
for i in range(n):
    l.remove(d[input().strip()])
print(len(l))
print(*l,sep="\n")
