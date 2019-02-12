t=int(input())
n,m=input().split()
n,m=int(n),int(m)
for u in range(t):
    l=[]
    for i in range(n):
          l.append(0)
    for i in range(m):        
        k=input().split()
        if k[0]=="UPDATE":
            l[int(k[1])]=int(k[4])
        if k[0]=="QUERY":
            print(sum(l[int(k[1]):int(k[-1])+1]))

        
