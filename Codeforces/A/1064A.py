import sys
input=sys.stdin.readline
l=list(map(int,input().split()))
l.sort()
if(l[0]+l[1]>l[2]):
    print(0)
else:
    print(l[2]-l[1]-l[0]+1)
