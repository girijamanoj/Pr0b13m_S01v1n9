import math
n,k=map(int,input().split())
t=240-k
h=int((math.sqrt(((8*t)/5)+1)-1)/2)

if(h>n):
    print(n)
else:
    print(h)

