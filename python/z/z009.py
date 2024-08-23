a = [17, 5, 3, 11, 16, 10, 23, 6, 8]
b, c = 0, 0
for j in range( len(a) ):
    for i in range( 1, len(a)-j ):
        b+=1
        if a[i-1]<a[i]:
            c+=1
            a[i-1], a[i] = a[i], a[i-1]
print( *a )
print( b )
print( c )