for _ in range( int(input()) ):
    n,r,c = map(int,input().split())
    r-=1; c-=1
    x,y = 0, n//2 + 1 - n%2
    for i in range(2, n**2+1):
        if x == r and y == c:
            print(i-1)
            break
        xx = n-1 if x == 0 else x-1
        yy = n-1 if y == 0 else y-1
        if (i-1)%n != 0 or i == 2:
            x,y = xx+0,yy+0
        else:
            x+=1
    else:
        print(n**2)