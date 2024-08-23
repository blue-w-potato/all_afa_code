def f( x, y ):
    
    n = 0
    bools = {}
    for i in range( 2, y+1 ):
        bools[i] = True
    
    for i in range( 2, y+1 ):
        if bools[i]:
            if i >= x:
                n += 1
            for i in range( i, y+1, i ):
                bools[i] = False
    return n

for i in range( int(input()) ):
    print( f(*map(int, input().split())) )