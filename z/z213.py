a=input()
print(abs(sum(list(map(int,a[1::2])))-sum(list(map(int,a[::2])))))