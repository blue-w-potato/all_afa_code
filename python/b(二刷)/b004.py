a = list(map(int,input().split()))
n = a.pop(0)
m = a.pop(0)
print( *sorted( list( set(range( 1, n+1 )) - set(a) ) ) )