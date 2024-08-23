a = list(map(int,input().split()[1:]))
m = a.pop(-1)
x,y = 0, 0
for i in a:
    if i>m:
        x+=1
    elif i<m:
        y+=1
print(x,y)