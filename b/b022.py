# 效率太好不能用 ( times 太少 )


ru = [ 0, 1 ]
def f(n):
    global ru
    if n < len(ru):
        return ru[n]
    a = f(n-1)
    b = f(n-2)
    ru.append(a+b)
    return ru[-1]

times = [ 1, 1, 3 ]
def ff(n):
    global times
    if n < len(times):
        return ( times[n] )
    ff( n-1 )
    a = times[n-1]
    b = times[n-2]
    times.append(a+b+1)
    return times[-1] 
a = int(input())
print(f(a), ff(a))
'''



4
3            2 
2       1    1   0
1   0

'''