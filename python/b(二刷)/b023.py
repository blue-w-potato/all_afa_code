def f( n, x, y, z ):
    if n == 1:
        print( f'Ring {n} from {x} to {z}' )
        return
    f( n-1, x, z, y )
    print( f'Ring {n} from {x} to {z}' )
    f( n-1, y, x, z )

f( int(input()), 1, 2, 3 )