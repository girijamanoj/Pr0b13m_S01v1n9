k=int(input())
d=0
if str(k).count('4')+str(k).count('7')==len(str(k)):
    print("YES")
    d=1
else:
    for i in range(k):
        if str(i).count('4')+str(i).count('7')==len(str(i)) and k%i==0:
            print("YES")
            d=1
            break
if d==0:
    print("NO")
