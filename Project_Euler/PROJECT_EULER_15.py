import math
t=int(input())
for i in range(t):
    l,k=map(int,input().split())
    print((math.factorial(l+k)//(math.factorial(l)*math.factorial(k)))%1000000007)
