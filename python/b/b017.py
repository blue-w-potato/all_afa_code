a=[]
while 1:
    try:
        a.append( list(map(int,input().split())) )
    except:
        break
print(a[0][0]*a[0][1] if len(a)==1 else a[0][0]*a[1][0])