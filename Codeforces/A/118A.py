k=input()
k=k.lower()
p=[]
for i in range(len(k)):
    if k[i]=='a' or k[i]=='e' or k[i]=='i' or k[i]=='o' or k[i]=='u' or k[i]=='y':
        True
    else:
        p.append('.'+k[i])
print(''.join(p))
