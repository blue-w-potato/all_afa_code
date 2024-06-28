a=int(input())
x=list(map(int,input().split()))
x1=[0 for i in range(10**6)]
i=0
while i<len(x)-1:
    x1[x[i]]=x[i+1]
    i+=2
b=int(input())
y=list(map(int,input().split()))
y1=[0 for i in range(10**6)]
i=0
while i<len(y)-1:
    y1[y[i]]=y[i+1]
    i+=2
for i in range(1001):
    x1[i]+=y1[i]
t=1
for i in range(10**6-1,-1,-1):
    if x1[i]:
        print(f'{i}:{x1[i]}')
        t=0
if t:print('NULL!')