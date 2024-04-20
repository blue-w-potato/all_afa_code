a=int(input())
c=0
v=a+0
while a>=5:
    c=a//5
    a=a%5+c
    v+=c
print(v)