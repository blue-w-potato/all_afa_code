n = int(input())
c = [0,1,5,10,50,100,500,1000,5000,10000]
dp = [[0 for i in range(n+1)] for j in range(len(c))]
for i in range(1,len(c)):
    for j in range(1,n+1):
        if c[i]==j:
            dp[i][j]=1
        elif c[i]>j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = 1 + dp[i][j-c[i]]
print(dp[-1][-1])