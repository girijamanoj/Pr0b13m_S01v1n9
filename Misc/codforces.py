n = list(map(int, input().split()))
m = n[1]
l = list(map(int, input().split()))
min = l[0] / l[1]
    
for i in range(n[0]-1):
    l = list(map(int, input().split()))
    if (min >= l[0] / l[1]):
        min = l[0] / l[1]
print(m*min)
