t = list(map(int, input().split()[1:]))
s = 0 
while len(t)>1:
    m1 = min(t)
    t.remove(m1)
    m2 = min(t)
    t.remove(m2)
    m = m1 + m2
    s += m
    t.append(m)
print(s)