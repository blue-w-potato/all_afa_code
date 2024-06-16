k=[0, 1, 1, 2]
def fff(n):
    if n==1:return 0
    if n<4:return 1
    global k
    if len(k)>n:
        return k[n]
    if len(k)<=n:
        k.append(fff(n-1) + fff(n-2))
    return k[n]
i=1
while k[-1]<1000000:
    fff(i)
    i+=1
k=sorted([1]+list(set(k)))
t=int(input())
for _ in range(t):
    a,b = map(int,input().split())
    c=[]
    for i in k:
        if i>b and i>a:
            break
        if i>=a and i<=b or i>=b and i<=a:
            c.append(i)
    for i in c:
        print(i)
    print(len(c))
    if _<t-1:print('------')