a = [101] + list(map(int,input().split()))
k = 0
for i in range(1, len(a)):
    ma = max(a[i:])
    mi = min(a[:i])
    if (mi < ma) and (ma - mi > k) and (abs(ma) >= abs(mi)):
        k = ma - mi
print(k)