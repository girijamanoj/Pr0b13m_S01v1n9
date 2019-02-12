import sys,math,string
input=sys.stdin.readline

L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split())
M=lambda : map(int,input().split())

n=int(input())
s=input().strip()
"""rgb
rbg
grb
gbr
brg
bgr"""
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
for i in range(0,n,3):
    p=s[i:i+3]

    if(p[0]=="R"):
        c5+=1
        c3+=1
        c4+=1
        c6+=1
    if(p[0]=="G"):
        c1+=1
        c2+=1

        c5+=1
        c6+=1
        
    if(p[0]=="B"):
        c1+=1
        c2+=1
        c3+=1
        c4+=1
    if(len(p)>1):
        if(p[1]=="R"):
            c1+=1
            c2+=1

            c4+=1

            c6+=1
        if(p[1]=="B"):
            c1+=1

            c3+=1

            c5+=1
            c6+=1
        if(p[1]=="G"):
            c5+=1
            c3+=1
            c4+=1
            c2+=1
    if(len(p)>2):
        if(p[2]=="R"):
            c1+=1
            c2+=1
            c3+=1
            c5+=1
        if(p[2]=="G"):
            c1+=1

            c3+=1
            c4+=1
            c6+=1
        if(p[2]=="B"):
            c5+=1
            c2+=1
            c4+=1
            c6+=1
if(min(c1,c2,c3,c4,c5,c6)==c1):
    k="RGB"*((n//3))+"RGB"[:n%3]
    print(c1)
    print(k)
elif(min(c1,c2,c3,c4,c5,c6)==c2):
    k="RBG"*((n//3))+"RBG"[:n%3]
    print(c2)
    print(k)
elif(min(c1,c2,c3,c4,c5,c6)==c3):
    k="GRB"*((n//3))+"GRB"[:n%3]
    print(c3)
    print(k)
elif(min(c1,c2,c3,c4,c5,c6)==c4):
    k="GBR"*((n//3))+"GBR"[:n%3]
    print(c4)
    print(k)
elif(min(c1,c2,c3,c4,c5,c6)==c5):
    k="BRG"*((n//3))+"BRG"[:n%3]
    print(c5)
    print(k)
elif(min(c1,c2,c3,c4,c5,c6)==c6):
    k="BGR"*((n//3))+"BGR"[:n%3]
    print(c6)
    print(k)
