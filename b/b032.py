a = list(map(int,input().split()))
n = a.pop(0)
dp = [ 1 for i in range(n+1)]
for i in range(n-1):
    for j in range(i+1,n):
        if a[j]>a[i]:
            dp[j] = max(dp[j],dp[i]+1)
print(max(dp))