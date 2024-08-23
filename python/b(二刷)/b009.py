a,b = input().split()
dp = [ [0 for i in range(len(b)+1)] for i in range( len(a)+1 ) ]
for i in range(len(a)):
    for j in range(len(b)):
        dp[i+1][j+1] = max( dp[i][j] + (a[i]==b[j]), dp[i+1][j], dp[i][j+1] )
        # for k in dp:print(*k)
        # print('='*100)

print( "YES" if dp[-1][-1] == len(a) else "NO")