x,y = map(int, input().split())
ru = [ [ 1 for i in range(x+1) ] ] + [ [1] + [ 0 for i in range(x) ]  for j in range(y)]
for i in range(1, y+1):
    for j in range(1, x+1):
        ru[i][j] = ru[i-1][j] + ru[i][j-1]
print(ru[-1][-1])