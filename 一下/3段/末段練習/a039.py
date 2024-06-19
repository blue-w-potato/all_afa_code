while 1:
    try:
        a,b = map(int,input().split())
        if a==b:print(0)
        elif a>b:print('A',a-b)
        else:print('B',b-a)

    except:
        break