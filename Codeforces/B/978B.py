import sys
input=sys.stdin.readline
L=lambda : list(map(int,input().split()))
M=lambda : map(int,input().split())
n=int(input())
s=list(input())
d=0
c=0
final=0
for i in range(n):
    if(s[i]=="x" and d==0):
        d=1
        c+=1
    elif((s[i]=="x" and d==1)):
         c+=1
    elif(s[i]!="x" and d==1):
         d=0
         if(c>=3):
             final+=(c-2)
         c=0
if(c>=3):
    final+=c-2
print(final)
        
    
