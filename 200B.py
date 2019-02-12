from sys import stdin, stdout
def main():
    
    n=int(stdin.readline())
    l=list(map(int,stdin.readline().split()))
    
    stdout.write(str(sum(l)/n))
            
if __name__ == "__main__": 
    main()
