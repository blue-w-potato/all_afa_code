for _ in range( int(input()) ):
    n,r,c = map(int,input().split())
    if (r%4 == 1 or r%4 == 0) and (c%4 == 1 or c%4 == 0) or (r%4 == 2 or r%4 == 3) and (c%4 == 2 or c%4 == 3):
        print((n-r)*n+(n-c+1))
    else:
        print((r-1)*n+c)