f = lambda x:x if x%2 else f(x//2)
print(f(int(input())))