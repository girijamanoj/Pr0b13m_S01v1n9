import sys
input=sys.stdin.readline
n=input()
l=list(input().split())
d=0
for i in l:
    if(n[0]==i[0] or n[1]==i[1]):
        print("YES")
        d=1
        break
if(d==0):
    print("NO")
