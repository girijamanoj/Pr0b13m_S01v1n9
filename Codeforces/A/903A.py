n=int(input())
for i in range(n):
    k=int(input())
    if k>11:
        print("YES")
    elif k%3==0 or k%7==0 or ((k%7)%3==0):
        print("YES")
    else:
        print("NO")
