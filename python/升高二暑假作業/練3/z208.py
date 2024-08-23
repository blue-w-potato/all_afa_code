n = int(input())
for i in range( 0,n ):
    print( ' '*((n*2-2*i)//2) + '*'*(1+2*i) +' '*((n*2-2*i)//2) )