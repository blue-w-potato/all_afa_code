a = list(map(int,input().split()[1:]))
s = 0
while 1:
    n = a.pop(a.index(min(a)))
    if not a:
        break
    j=a.index(min(a))
    a[j]+=n
    s+=a[j]
print(s)