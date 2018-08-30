n,x,y = map(int, input().split(' '))
st = set()
for i in range (n):
    a,b=map(int, input().split())
    st.add((a-x)/(b-y) if b != y else float("INF"))
print (len(st)) 
