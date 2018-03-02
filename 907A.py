k=list(map(int,input().split()))
if k[3]<=(2*k[2]):
    print(k[0])
    print(k[1])
    if k[2]>k[3]:
        print(k[2])
    else:
        print(k[3])
else:
    print(-1)
