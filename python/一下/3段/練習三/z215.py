a,b,c = map(int,input().split())
if a>b:a,b=b,a
if b>c:b,c=c,b
if a>b:a,b=b,a
print(a,b,c)
a*=a
b*=b
c*=c
if a**0.5+b**0.5<=c**0.5:print('No')
elif a+b==c:print('Right')
elif a+b<c:print('Obtuse')
else:print('Acute')