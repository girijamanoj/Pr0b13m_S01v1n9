s,n=map(int,input().split())
l=[] # empty list
for i in range(n):
    l.append(list(map(int,input().split()))) # inserting a list to the list l making more sense just creating a 2d array
l.sort()
for i,j in l: # l is a list here
    s=(s+j)*(s>i)
print('YNEOS'[(s<1)::2]) # string slicing     
    
    
