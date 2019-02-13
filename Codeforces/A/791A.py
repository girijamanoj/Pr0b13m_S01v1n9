import sys,math,string
input=sys.stdin.readline

L=lambda : list(map(int,input().split()))
M=lambda : map(int,input().split())

a,b=M()
i=1
while(a*pow(3,i)<=b*pow(2,i)):
    i+=1
print(i)
    
