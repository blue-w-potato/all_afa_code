ru = lambda x,y, n=0: n if x*(3**n)>=y else ru( x, y, n=n+1 )
print(ru(*map(int,input().split())))