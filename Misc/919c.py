import sys
line=sys.stdin.readline().split()
n=int(line[0])
m=int(line[1])
mprice=100000
for j in range(n):
    l=sys.stdin.readline().split()
    price = m*int(l[0])/int(l[1])

    if price < mprice:
        mprice=price         
print(mprice)
