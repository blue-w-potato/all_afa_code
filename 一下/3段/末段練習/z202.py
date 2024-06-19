while 1:
    a,b,c = map(int,input().split())
    if a==b==c==0:
        break
    print(len([0 for i in range(a,b+1) if sum(list(map(int,list(str(i)))))%c==0]))