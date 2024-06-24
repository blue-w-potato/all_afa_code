n,m = map(int,input().split())
a = list(map(int,input().split()))
k = []
def yee(n, array, data):
    global m
    if n == m:
        global k
        k.append(data[:])
        return
    if n>m or n<m and len(array)==0:
        return
    for i in range(len(array)):
        c = array[i]
        aa = array[i+1:]
        data.append(c)
        yee(n+c, aa, data)
        data.remove(c)
        
for i in range(n-1):
    c = a[i+1:]
    yee(a[i], c, [a[i]])

    
for i in k:
    print(*i)
if len(k) == 0:
    print('NO')