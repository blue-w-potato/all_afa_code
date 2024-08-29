a, b = map( int, input().split() )
def f( x, y ):
    if x == 0 or y == 0:
        return 1
    s = 0
    if x > 0:
        s += f( x-1, y )
    
    if y > 0:
        s += f( x, y-1 )
    return s
print( f( a, b ) )