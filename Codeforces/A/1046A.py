import sys
input=sys.stdin.readline
print=sys.stdout.writelines
n,k=map(int,input().split())
l=[]
c=0
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n-1):
    for j in range(i+1,n):
        p1=l[i]
        p2=l[j]
        if((p2[0]<=p1[0]+p1[1] and p2[0]>=p1[0]-p1[1]) and (p1[0]<=p2[0]+p2[1] and p1[0]>=p2[0]-p2[1])):
            if(abs(p2[2]-p1[2])<=k):
                c+=1
print(str(c))
