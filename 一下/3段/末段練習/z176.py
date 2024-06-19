while 1:
    n = int(input())
    if n == 0:break
    k = n**0.5
    if k%1==0:
        if n%2:
            print(1,int(k))
        else:
            print(int(k),1)
    else:
        a = int((k-1)//1+1)
        b = int(k//1+1)
        if k-a < b-k:
            if a%2:
                print( n-a**2, b )
            else:
                print( b, n-a**2 )
                
        else:
            if b%2:
                print( b**2-n+1, a+1 )
            else:
                print( a+1, b**2-n+1 )