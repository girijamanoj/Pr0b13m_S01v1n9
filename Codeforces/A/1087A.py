t=input()
if(len(t)%2==0):
    l=len(t)//2-1
    r=len(t)//2
else:
    l=len(t)//2
    r=len(t)//2+1
s=""
while(l>=0 and r<len(t)):
    s+=t[l]+t[r]
    l-=1
    r+=1
if(l==0):
    s+=t[l]
elif(r==len(t)-1):
    s+=t[r]
print(s)
