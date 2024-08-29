data = [ [0, 1], [1, 1] ]
def f( n ):
    global data
    if n < len(data):
        return data[n]
    a = f( n-1 )
    b = f( n-2 )
    data.append( [ a[0]+b[0], a[1]+b[1]+1 ] )
    return data[n]

a = f(int(input()))
print( *a )