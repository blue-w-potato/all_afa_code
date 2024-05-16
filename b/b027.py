t = int(input().split()[0])
a = [ list(map(int,input().split())) for i in range(t) ]
dp = [ [ 0 for i in range(len(a[0])) ] for j in range(t) ]

for i in range(1, t):
    for j in range(1, len(a[0])):
        if a[i][j] == 0:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) +1

ru = []
for i in dp:ru+=i
print(max(ru)**2)