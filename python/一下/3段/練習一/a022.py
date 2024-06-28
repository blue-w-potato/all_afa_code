a = lambda x,y, n=0: n if x*(3**n)>=y else a( x, y, n=n+1 )
print(a(*map(int,input().split())))


