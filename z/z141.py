a = [eval(input()) for i in range(3)]
a.sort()
if sum(a[:2])>a[2]:
    print(sum(a))
else:
    print('Invalid')