a = list(map(int,input().split()[1:]))
s = 0
while 1:
    n = a.pop(a.index(min(a)))
    if not a:
        break
    s+=len(a)*n
print(s*100)