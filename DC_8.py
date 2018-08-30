R=lambda:map(int,input().split())
n,d=R()
h=2
a=R()
p=next(a)
for x in a:
 h+=(x-p>=d*2)+(x-p>d*2);p=x
print(h)
