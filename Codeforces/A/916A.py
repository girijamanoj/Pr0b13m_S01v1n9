t=int(input())
n,m=input().split()
p,k=int(n),int(m)
d=0
s=0
l=0
while d!=1:
    if k>10:
        if str(k)[0]=='7' or str(k)[1]=='7':
            if s%t==0:
                print(s//t)
                l=1
                d=1
                break
    elif k<10:
        if str(k)[0]=='7':
            if s%t==0:
                print(s//t)
                l=1
                d=1
                break
    if p>10:           
        if str(p)[0]=='7' or str(p)[1]=='7':
            if l==0:
                if s%t==0:
                    print(s//t)
                    l=1
                    d=1
                    break
    elif p<10:
        if str(p)[0]=='7':
            if l==0:
                if s%t==0:
                    print(s//t)
                    l=1
                    d=1
                    break
        
    if k!=0:        
        k=(k-1)%60
    elif k==0:
        k=59
        p=(p-1)%24
    elif p==0 and k==0:
        p=23
        k=59
        
    s+=1    
        
        
    
        
            
        
        
          
    
             
