s = int(input())
dp = [0 for j in range(s+1)]
for i in range(1, s+1):
    if i < 3:
        dp[i] = i
    else:
        dp[i] = dp[i-1] + dp[i-2]
c1 = dp[-1]
s = c1%s
dp = [0 for j in range(s+1)]
for i in range(1, s+1):
    if i < 3:
        dp[i] = i
    else:
        dp[i] = dp[i-1] + dp[i-2]
c2 = dp[-1]
print(c1, c2)