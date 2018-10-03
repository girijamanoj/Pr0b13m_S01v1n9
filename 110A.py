p=int(input()) #taking input and typecasting it
k=str(p)
if str(k.count('7')+k.count('4')).count('7')+str(k.count('7')+k.count('4')).count('4')==len(str(k.count('7')+k.count('4'))):
    print("YES")
else:
    print("NO")
