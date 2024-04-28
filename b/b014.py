a = [ sum(map(int,input().split())) for i in range(3) ]
print(a.index(max(a))+1,max(a))