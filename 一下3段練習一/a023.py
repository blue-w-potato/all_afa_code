a = lambda x, n=1: n if x==1 else (a(x*3+1, n=n+1) if x%2 else a(x//2, n=n+1))
print(a(int(input())))


