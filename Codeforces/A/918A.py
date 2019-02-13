import sys,math
input=sys.stdin.readline
print=sys.stdout.write
L=lambda : list(map(int,input().split().strip()))
M=lambda : map(int,input().split())
a=int(input())
f=["o"]*max(3,(a+1))
f[1]="O"
f[2]="O"
f1=1
f2=1
while(f2<a):
    x=f2+f1
    if(x>a):
        break
    f[x]="O"
    f1=f2
    f2=x
for i in range(1,a+1):
    print(f[i])
    
