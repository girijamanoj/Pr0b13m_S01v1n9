k=input()
l=k.split('+')
l=sorted(list(map(int,l)))
l=list(map(str,l))
print("+".join(l))

