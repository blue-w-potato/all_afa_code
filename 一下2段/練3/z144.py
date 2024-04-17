a = eval(input())
b = eval(input())
print(sum([i for i in range(a+a%2,b+1,2)]))