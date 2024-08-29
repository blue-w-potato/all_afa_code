a = list(map(int, input().split()[1:]))
for i in range( 1, len(a) ):
    a[i] += max( 0, a[i-1] )
s =  max(a) 
print( s if s>0 else 0 )