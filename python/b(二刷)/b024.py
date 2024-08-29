data = [ 0, 1, 2 ]
n = int(input())
def f( n ):
    global data
    if n < len(data):
        return data[n]
    data.append( f(n-2) + f(n-1) )
    return data[n]
k = f(n)
print(k,f(k%n))