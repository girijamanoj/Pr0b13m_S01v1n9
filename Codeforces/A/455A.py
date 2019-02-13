n=int(input())
l=list(map(int,input().split()))
g=[0]*(max(l)+1)
for i in range(len(l)):
    g[l[i]]+=1
for i in range(2,len(g)):
    left_max=max(g[i-1],g[i-2]+g[i]*i)
    g[i]=left_max
print(g[-1])
    
