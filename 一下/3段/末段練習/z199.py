a=int(input())
b=int(input())
t = [[]]
k = []
for i in range(a,b+1):
    if i %9==0 or i %4==0:
        k.append(i)
        t[-1].append(f'{i:<4}')
        if len(t[-1])==10:
            t.append([])
for i in t:
    for j in i:
        print(j,end='')
    print()
print(len(k))
print(sum(k))