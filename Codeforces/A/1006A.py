n=int(input())
l=list(map(int,input().split()))
for i in l:
    if(i%2==0):
        i=i-1
    print(i,end=" ")
