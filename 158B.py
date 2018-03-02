n=int(input())
l=list(map(int,input().split()))
four=l.count(4)
three=l.count(3)
two=l.count(2)
one=l.count(1)
p=abs(one-three)
if three>=one:
    print(four+one+(three-one)+(two//2)+(two%2))
else:
    if p//2>=two:
        print(four+three+two+(((p)-two)//4)+(((p)-two)%4))
    else:
        print(four+three+(p//2)+((two-p//2)//2)+((two-p//2)%2))
