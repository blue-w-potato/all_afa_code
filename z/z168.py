def qwer():
    a = [ 1 for i in range(65537) ]
    for i in range(2,65537):
        if a[i]:
            for j in range( i**2, 65537, i ):
                a[j] = 0
    return [ i for i in range( 2, 65537 ) if a[i] ]
znums = qwer()

for _ in range(int(input())):
    a,b = map(int, input().split())
    n=a+0
    
    if b>a:a,b=b,a
    while 1:
        a%=b
        if a==0:
            break
        if b>a:a,b=b,a
    
    k = [  ]
    for i in znums:
        if i > n:break
        if n%i==0:
            k.append([i, 0]) 
            while n>=i and n%i == 0:
                k[-1][-1]+=1
                n//=i
    for i in range(len(k)):
        if k[i][-1] == 1:
            k[i] = k[i][:1]
    print('*'.join(list(map(lambda x: '^'.join(list(map(str,x))), k))), ',', b, ',', 'Y' if b in znums else 'N')