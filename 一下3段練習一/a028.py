a = lambda x: x if x<3 else a(x-1)*x
n,r = map(int,input().split())
print(a(n)//a(n-r))

