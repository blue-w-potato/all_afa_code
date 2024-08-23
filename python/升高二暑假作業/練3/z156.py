for _ in range(int(input())):
    n = input()
    a = list( map( int, list(n) ) )
    print( f"Sum of all digits of {n} is {sum(a)}" )