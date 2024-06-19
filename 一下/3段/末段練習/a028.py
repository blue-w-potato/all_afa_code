f = lambda x:x if x<3 else f(x-1)*x
a,b = map(int,input().split())
print(f(a)//f(a-b))