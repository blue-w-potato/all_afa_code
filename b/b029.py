c = (0, 2,5,10,20,25)
n = int(input())
dp = [ [1] + [0 for i in range(n)] for j in range(6)]
for i in range(1,6):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j]
        if j >= c[i]:
            dp[i][j] += dp[i][j-c[i]]
print(dp[-1][-1])