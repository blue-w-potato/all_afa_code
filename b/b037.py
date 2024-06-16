k=[]
def yee(a,b,c):
    if len(a)==c:
        global k
        k.append(a)
        return
    b=list(b)
    for i in b:
        yee(a+i,b,c)
    return
a,b=map(int,input().split())
yee('',[str(i) for i in range(b+1)],a)
for i in k:print(i)