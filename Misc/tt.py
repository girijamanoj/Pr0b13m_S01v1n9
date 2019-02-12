import math
t=4294967288
i=1
while (i<=math.sqrt(t)):
    if (t%i==0):
        print(i,"<====>",((t//i)-i))
    i+=1
