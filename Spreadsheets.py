import re
import math
def wer(num):
    c=''
    while num:
        mod = (num - 1) % 26
        c+= chr(mod + 65)
        num = (num - 1) // 26
    return ''.join(reversed(c))
n=int(input())
for i in range(n):
    k=input()
    l=re.split('(\d+)',k)
    if l[0]=='R':
        j=int(l[3])
        c=wer(j)+l[1]
        print(c)    
    else:
        col=0
        for i in range(len(l[0])):
            d=ord(l[0][i])
            col=col+(d-64)*(pow(26,len(l[0])-1-i))
        print('R'+l[1]+'C'+str(col))
                
