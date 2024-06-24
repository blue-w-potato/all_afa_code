n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
x = sum(a)/n; y = sum(b)/n
r=1
for i in range(n):
    if a[i]>=x and b[i]>=y:
        print(i+1, end = ' ')
        r=0
if r:
    print('NO')