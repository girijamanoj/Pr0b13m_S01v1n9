"""this is a codeforces problem
http://codeforces.com/problemset/problem/112/A"""
n=input()
m=input()
n,m=n.lower(),m.lower()
d=0
for i in range(len(n)):
    if n[i]<m[i]:
        print("-1")
        d=1
        break
    elif n[i]>m[i]:
        print("1")
        d=1
        break
if d==0:
    print("0")
            
