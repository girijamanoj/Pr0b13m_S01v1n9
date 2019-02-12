k=list(map(int,input().split()))
p=(k[0]*((k[2]*(k[2]+1))//2))-k[1]
print(p if p>0 else '0')
