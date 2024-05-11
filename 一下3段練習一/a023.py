ru = lambda x, n=1: n if x==1 else (ru(x*3+1, n=n+1) if x%2 else ru(x//2, n=n+1))
print(ru(int(input())))