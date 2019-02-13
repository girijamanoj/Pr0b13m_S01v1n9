n = int(input())
m = n - 1
pos = reversed(sorted(map(int,input().split())))
odd = 0;even = 0
for p in pos:
    even+=abs(n-p)
    n-=2
    odd+=abs(m-p)
    m-=2
print (min(odd,even))
