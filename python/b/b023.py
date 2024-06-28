def river( n, x, y, z ):
    if n == 1:
        print( f'Ring 1 from {x} to {y}' )
        return
    river( n-1, x, z, y )
    print( f'Ring {n} from {x} to {y}' )
    river( n-1, z, y, x )
river(int(input()), 1, 3, 2)