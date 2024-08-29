s = 0
for _ in range(3):
    a = list(input())
    i = 0
    while i<len(a):
        try:
            a[i] = str(int(a[i]))
            i+=1
        except:
            a.remove(a[i])
    s += int( ''.join(a) )
print(s)