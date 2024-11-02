s = list(map(int, input().split()))
n = s.pop(0)
dp = [1 for i in range(n)]
for i in range(n-1):
    for j in range(i+1, n):
        if s[j] > s[i] and dp[j] < dp[i]+1:
            dp[j] = dp[i]+1
print(max(dp))