import string
l=input()
if l.isupper():
    print(l.lower())
elif l[1:].isupper():
    print(l.capitalize())
else:
    if len(l)!=1:
        print(l)
    else:
        print(l.upper())
