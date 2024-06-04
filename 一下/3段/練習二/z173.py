def qwer():
    a = [ 1 for i in range(10**5+1) ]
    n = [ ]
    for i in range(2,10**5+1):
        if a[i]:
            n.append(i)
            for j in range( i**2, 10**5+1, i ):
                a[j]=0
    return n

znums = qwer()
while 1:
    try:
        a = list(input())
        k = []
        s = 0; e = 1
        while e<=len(a):
            b=int(''.join(a[s:e]))
            if b == 0:
                s=e; e+=1
            elif b == 1:
                e+=1
            elif b in znums:
                k.append(b)
                s=e; e+=1
            else:
                r = int(b**0.5)+1
                for i in znums:
                    if i > r:
                        k.append(b)
                        s=e; e+=1
                        break
                    if b%i == 0:
                        e+=1
                        break
        print(len(k))
        if len(k):
            for i in k:
                print(i)
        print()
    except EOFError:
        break