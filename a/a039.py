while 1:
    try:
        a,b=map(int,input().split())
        if a==b:
            print(0)
        else:
            print('A'if a>b else 'B', max(a,b)-min(a,b))
    except:
        break