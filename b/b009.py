a,b=input().split()
dp=[[0 for i in range(len(a)+1)] for i in range(len(b)+1)]
for i in range(1,len(b)+1):
    for j in range(1,len(a)+1):
        dp[i][j]=max(dp[i-1][j-1]+(a[j-1]==b[i-1]),dp[i-1][j],dp[i][j-1])
print('YES'if dp[-1][-1]==len(a) else 'NO')