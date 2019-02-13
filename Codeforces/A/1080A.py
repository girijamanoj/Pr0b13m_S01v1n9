import sys
import math
input=sys.stdin.readline
n,k=map(int,input().split())
print(math.ceil(n*2/k)+math.ceil(n*5/k)+math.ceil(n*8/k))
