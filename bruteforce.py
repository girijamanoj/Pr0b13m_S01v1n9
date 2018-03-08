
def wer(num):
    c=''
    while num:
        mod = (num - 1) % 26
        c+= chr(mod + 65)
        num = (num - 1) // 26
    return ''.join(reversed(c))
d={}
for i in range((10**5)+1):
    d1={i:wer(i)}
    d.update(d1)
print(d)    
    
