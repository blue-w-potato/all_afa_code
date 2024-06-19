a,b = map(int,input().split())
print(len([1 for i in range(a,b+1) if i%5 and i%2 and i%3]))