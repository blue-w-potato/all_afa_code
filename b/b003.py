ru=list(map(int,input().split()[1:]))
a,b=0,0
for i in ru[:-1]:
    if i>ru[-1]:
        a+=1
    elif i<ru[-1]:
        b+=1
print(a,b)