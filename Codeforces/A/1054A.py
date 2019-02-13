import sys

input=sys.stdin.readline

x,y,z,t1,t2,t3=map(int,input().split())
time=abs(x-z)*t2+t3*2+abs(y-x)*t2+t3
d=abs(x-y)*t1
if(time<=d):
    print("YES")
else:
    print("NO")
