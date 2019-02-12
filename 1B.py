for n in range(int(input())):

    x = input();char=numb=0

    for c in x:

        if '0' <= c<='9':
            numb=10*numb+int(c)
        elif numb:

            char,numb=x[1:].split('C')
            numb=int(numb)
            t=""
            while numb:
                numb-=1
                t=chr(65+numb%26)+t
                numb//=26

            print(t+char)
            break

        else:
            char=26*char+ord(c)-64

    else:
        print("R%dC%d" % (numb, char))
