a = list(map(int,input().split()[1:]))
dp = [[1 for i in range(len(a))] for j in range(len(a))]
for i in range(0, len(a)-1):
    n = a[i]
    for j in range(i, len(a)):
        dp[i][j] = dp[i][j-1] 
        if n < a[j]:
            dp[i][j] += 1
            n=a[j]
print(max([ i[-1] for i in dp ]))