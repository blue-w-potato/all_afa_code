n, p = map( int, input().split() )
a = [0]+list(map(int,input().split()))
s = 0
for i in range( p ):
    x, y = map( int,input().split() )
    s += max(a[ x:y+1 ])
print( s )