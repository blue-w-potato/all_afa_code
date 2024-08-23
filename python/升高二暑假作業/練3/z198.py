a=float('inf')
while 1:
    n = eval(input())
    if n == 9999:break
    a = min(a,n)
print(a)