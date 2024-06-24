a = list(map(int,input().split()))
n = a.pop(0)
for i in range(1, n):a[i] = max(a[i], a[i]+a[i-1])

print(max(a) if max(a)>0 else 0)