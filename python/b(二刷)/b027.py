m = 0
h, w = map(int,input().split())
a = [ list(map(int,input().split())) for i in range( h ) ]
dp = [ [ 0 for i in range( w+1 ) ] for i in range( h+1 ) ]
for i in range( 1, h+1 ):
    for j in range( 1, w+1 ):
        if (a[i-1][j-1] == 0):
            dp[i][j] =  1 + min( dp[i-1][j], dp[i][j-1], dp[i-1][j-1] )
            if dp[i][j] > m:
                m = dp[i][j]+0

print(m**2)