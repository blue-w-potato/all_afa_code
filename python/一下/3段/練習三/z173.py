def yee( n=10**5 ):
    a = [ True for i in range(n+1) ]
    b=[]
    for i in range(2,n+1):
        if a[i]:
            b.append(i)
            for j in range(i**2,n+1,i):
                a[j] = False
    return b

w=yee()

while 1:
    try:
        a=input()
        k=[]
        s=0;e=1
        while 1:
            if e>len(a):
                break
            n=int(a[s:e])
            if n == 0:
                s+=1
                e+=1
            elif n==1:
                e+=1
            elif n in w:
                k.append(n)
                s=e+0;e+=1
            else:
                for i in w:
                    if i>int(n**0.5)+1:
                        k.append(n)
                        s=e+0;e+=1
                        break
                    if n%i==0:
                        e+=1
                        break
        print(len(k))
        for i in k:
            print(i)
        print()
    except:
        break