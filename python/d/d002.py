a=(lambda x,y,a,b:(a-x)*60+b-y)(*map(int,input().split()))
if a<=30:
    print(0)
else:
    if a<=60:
        print(30)
    else:
        if a<=120:
            print(60)
        else:
            print(a//60*30+30 if a//60*30+30<210 else 210)