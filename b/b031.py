n,m = map(int,input().split())
ru = []
for i in range(n):
    ru.append(list(map(int,input().split())))
ru.sort(key=lambda x: x[0])
ru = [[0, 0]] + ru
dp = [[0 for i in range(m+1)] for j in range(len(ru))]
for i in range(1, len(ru)):
    for j in range( 1, m+1 ):
        if i == 1:
            dp[i][j] = ru[i][1] * ( j//ru[1][0] )
        elif ru[i][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max( dp[i-1][j], dp[i-1][j-ru[i][0]] + ru[i][1]  )
# for i in dp:
#     print(*i)
print(dp[-1][-1])