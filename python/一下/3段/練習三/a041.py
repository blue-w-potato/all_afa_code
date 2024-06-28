a = int(input())
if a<5:
    print(a)
else:
    b=a+0
    while a>=5:
        b+=a//5
        a=a-(a//5)*5+a//5
    print(b)