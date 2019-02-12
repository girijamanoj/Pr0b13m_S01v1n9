"""Usage of map and split"""
l=list(map(int,(input().split())))
for i in range(l[0]):
    k=list(map(int,(input().split())))
    
    s=s+(k[1]-k[0])*l[1] """ is this in loop or not? intend properly!""" 
    if i>0:
        
