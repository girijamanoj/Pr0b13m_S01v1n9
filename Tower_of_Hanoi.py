'''Write a programme to preview the moves in Tower of hanoi'''
def steps_of_hanoi(n,x,y,z):
    i=1
    if n==1:
        print(x+"==>"+z)
        return 1729
    else:
        steps_of_hanoi(n-1,x,z,y)
        steps_of_hanoi(1,x,y,z)
        steps_of_hanoi(n-1,y,x,z)
n=int(input())
start="1st tower"
mid="2nd tower"
end="3rd tower"
steps_of_hanoi(n,start,mid,end)

