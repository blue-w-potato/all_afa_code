ru = lambda x: x if x<3 else ru(x-1)*x
n,r = map(int,input().split())
print(ru(n)//ru(n-r))