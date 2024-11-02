n, m = map(int, input().split())
ru = []
for i in range(n):
    ru.append(list(map(int,input().split())))
ru.sort(key = lambda x: x[1], reverse=True)
ru.sort(key = lambda x: x[0])
ru = [[0,0]] + ru
dp = [0 for i in range(m+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if ru[i][0] > j:
            continue
        else:
            dp[j] = max(dp[j],dp[j-1] , ru[i][1] + dp[j-ru[i][0]], ru[i][1]*(j//ru[i][0]) )
print(dp[-1])