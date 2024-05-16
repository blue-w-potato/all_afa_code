a = int(input())
b = [0, 1, 5, 10, 12, 16, 20]
# 1元、5元、10元、12元、16元、20元
dp = [[0 for i in range(a+1)]] + [ [0]+[ i for i in range(a) ] for j in range(6) ]
for i in range(1, 7):
    for j in range(1, a+1):
        if i == 1:
            dp[i][j] = j    
        elif j == b[i]:
            dp[i][j] = 1
        elif j > b[i]:
            dp[i][j] = min(dp[i][j-b[i]] + dp[i][b[i]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
# for i in dp:
#     for j in i:
#         print(f"{j:>2}",end='  ')
#     print()
print(dp[-1][-1])