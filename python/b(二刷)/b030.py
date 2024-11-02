n, m = map(int, input().split())
ru = []
for i in range(n):
    ru.append(list(map(int,input().split())))
ru.sort(key = lambda x: x[0])
ru = [[0,0]] + ru
dp = [ [0 for i in range(m+1)] for j in range(n+1) ]
for i in range(1, n+1):
    for j in range(1, m+1):
        if ru[i][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], ru[i][1] + dp[i-1][j-ru[i][0]] )
print(dp[-1][-1])
# for i in dp:print(i)