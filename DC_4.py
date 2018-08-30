t=int(input())
p=input()
q=set(p)
if(len(p)>26):
    print(-1)
else:
    print(t-len(q))
