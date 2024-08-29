c = [ 1, 5, 10, 12, 16, 20 ]
m = int(input())
dp = [ [ 0 for i in range( m+1 ) ] for j in range( len(c)+1 ) ]
for i in range( 1, len(c)+1 ):
    for j in range( 1, m+1 ):
        if i == 1:
            dp[i][j] = j
        elif j < c[i-1]:
            dp[i][j] = dp[i-1][j]
        elif j == c[i-1]:
            dp[i][j] = 1
        else:
            dp[i][j] = min( dp[i][c[i-1]] + dp[i][j-c[i-1]], dp[i-1][j] )
print( dp[-1][-1] )