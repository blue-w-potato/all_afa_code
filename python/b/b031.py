n,m = map(int,input().split())
L = []
S = []
for i in range(n):
    a=list(map(int,input().split()))
    L.append(a[0])
    S.append(a[1])
dp = [0 for i in range(m+1)]
for i in range(n):
    for j in range(1,m+1):
        if j>=L[i]:
            dp[j] = max(dp[j],dp[j-L[i]] + S[i])
        else:
            dp[j] = max(dp[j],dp[j-1])
print(dp[-1])