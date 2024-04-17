a = eval(input())
if a<5:print(0)
else:print(sum([i for i in range(5,a+1,5)]))