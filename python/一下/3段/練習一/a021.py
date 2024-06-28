a = lambda x: x if x%2 else a(x//2)
print(a(int(input())))