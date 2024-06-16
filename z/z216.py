n = int(input().split()[0])
h = [max(list(map(int,input().split()))) for i in range(n)]
m = sum(h)
print(m)
g = [ i for i in h if m%i==0]
if g:print(*g)
else:print(-1)