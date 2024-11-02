t = list(map(int, input().split()))
n = t.pop(0)
s = 0
while t:
    m = min(t)
    t.remove(m)
    s+=len(t)*m
print(s*100)