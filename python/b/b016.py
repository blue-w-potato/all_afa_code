a=[]
while 1:
    try:
        a.append( sum(map(int,input().split())) )
    except:
        break
print(sum(a))