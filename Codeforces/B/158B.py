import sys
input=sys.stdin.readline
print=sys.stdout.write

n=int(input())
l=list(map(int,input().split()))
c1=0
c2=0
c3=0
c4=0
for i in range(n):
    if(l[i]==1):
        c1+=1
    elif(l[i]==2):
        c2+=1
    elif(l[i]==3):
        c3+=1
    else:
        c4+=1
x=c4
c1-=min(c1,c3)
x+=c3

f=False
if(c1%2==1):
    f=True
pairs1=c1//2
if(pairs1>=c2):
    x+=c2
    remained=2*(pairs1-c2)+f
    x+=(remained//4)+int(bool(remained%4))
else:
    x+=pairs1
    c2=c2-pairs1
    c1=f
    k=0
    if(c2%2==1):
        k=1
    x+=c2//2
    x+=int(bool(c1+k))
print(str(x))
        
    
