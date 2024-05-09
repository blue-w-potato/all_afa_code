ru = [101] + list(map(int,input().split()))
k = 0
for i in range(1, len(ru)):
    if min(ru[:i]) < max(ru[i:]) and max(ru[i:]) - min(ru[:i]) > k and max(ru[i:]) + min(ru[:i]) > 0:
        k = max(ru[i:]) - min(ru[:i])
print(k)