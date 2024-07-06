from math import gcd
a,b=map(int,input().split(","))
x,y=map(int,input().split(","))
print(f'{a}/{b} + {x}/{y} = ', end='')
a=a*y+x*b; b*=y
k=gcd(a,b)
a//=k; b//=k
if a<0 and b>0 or a<0 and b<0:
    a*=-1; b*=-1
print(f'{a}/{b}')