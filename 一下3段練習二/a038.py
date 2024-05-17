while 1:
    a,b = map(int,input().split())
    if a==0 and b==0:
        break
    print( 0 if a==b else( 'A' if a>b else 'B' ) + ' ' + str(abs(a-b)) )