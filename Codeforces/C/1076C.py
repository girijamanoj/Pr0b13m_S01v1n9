import math
t=int(input())
for i in range(t):
    d=int(input())
    if(d**2>=4*d):
        print("Y",'{0:.9f}'.format(round((math.sqrt(d**2-4*d)+d)/2,9)),'{0:.9f}'.format(round((-math.sqrt(d**2-4*d)+d)/2,9)))
    else:
        print("N")
