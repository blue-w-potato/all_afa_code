ru = lambda x: x if x%2 else ru(x//2)
print(ru(int(input())))