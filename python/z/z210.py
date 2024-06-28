while 1:
    try:
        a=int(input())
        s=0
        while a!=1:
            s+=1
            if a%2:
                a*=3
                a+=1
            else:
                a//=2
        print(s)
    except:
        break