k=[]
def yee(a,b,c):
    if len(a)==c:
        global k
        k.append(a)
        return
    b=list(b)
    for i in b:
        bb=b.copy()
        bb.remove(i)
        yee(a+i,bb,c)
    return
n=int(input())
yee('',[str(i) for i in range(1,n+1)],n)
for i in k:print(i)