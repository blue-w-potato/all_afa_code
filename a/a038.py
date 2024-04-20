while 1:
    a,b=map(int,input().split())
    if a==b==0:
        break
    if a==b:
        print(0)
    else:
        print('A'if a>b else 'B', max(a,b)-min(a,b))