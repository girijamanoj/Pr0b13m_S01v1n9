import sys
input=sys.stdin.readline
l=list(map(int,input().split()))
s=0
while(l[-1]):
    s+=2*(l[0]+l[1]-2)
    l[-1]-=1
    l[0]-=4
    l[1]-=4
    if(l[0]*l[1]<=0):
        break
print(s)
