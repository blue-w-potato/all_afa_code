f = lambda x: x if x<3 else x*f(x-1)
print(f(int(input())))