
import string
n,m=input().split()
n,m=int(n),int(m)
k=input()
while m>0:
    k=k.replace("BG","GB")
    m-=1
print(k)
