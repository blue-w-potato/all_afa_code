a,b = map(int,input().split())
print(a,end='')
for i in range(a+1,b+1):
    print('+',end=str(i))
print('=',end=str(sum([i for i in range(a,b+1)])))