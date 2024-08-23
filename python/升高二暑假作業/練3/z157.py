a = float(input())
b = float(input())
c = int(input())
print( "Month 	  Amount" )
for i in range( 1, c+1 ):
    a += ( a*b/1200 )
    k = a*100 //1 /100 + (a*100%1>=0.5)*0.01
    print( f'  {i} 	 {k:.2f}' )
    
    