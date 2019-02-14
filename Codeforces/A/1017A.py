import sys
input=sys.stdin.readline
n=int(input())
k=sum(list(map(int,input().split())))
s=[k]
for i in range(1,n):
    s.append(sum(map(int,input().split())))
s.sort(reverse=True)
print(s.index(k)+1)
    
    

