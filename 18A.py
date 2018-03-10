from math import sqrt
l=list(map(int,input().split()))
x=sqrt(((l[2]-l[0])**2)+((l[3]-l[1])**2))
y=sqrt(((l[4]-l[2])**2)+((l[5]-l[3])**2))
z=sqrt(((l[4]-l[0])**2)+((l[5]-l[1])**2))
if (max(x,y,z))**2=((x+y+z)-max(x,y,z)-min(x,y,z))**2+(min(x,y,z)**2):
    print("RIGHT")
else:
x=sqrt(((l[2]+1-l[0])**2)+((l[3]-l[1])**2))
y=sqrt(((l[4]-l[2]+1)**2)+((l[5]-l[3])**2))
z=sqrt(((l[4]-l[0])**2)+((l[5]-l[1])**2))
a=sqrt(((l[2]-l[0])**2)+((l[3]-l[1])**2))
b=sqrt(((l[4]-l[2])**2)+((l[5]-l[3])**2))
c=sqrt(((l[4]-l[0])**2)+((l[5]-l[1])**2))
