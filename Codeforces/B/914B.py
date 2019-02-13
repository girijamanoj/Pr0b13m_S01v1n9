n=int(input())
k=list(map(int,input().split()))
k.sort()
p=k.count(max(k))
if p%2==0:
    print("Agasa")
else:
    print("Conan")
        
