from math import log
a,b = map(int,input().split())
f = lambda x: True if x == 10 else (f(x//10) if x%10 ==0 else False)
k = lambda x,y=1: y if x==10 else k(x//10, y+1)
if a == 1:
    print(1)
elif b == 1:
    print(len(str(a)))
elif f(a):
    print(k(a)*b)
else:
    print( int(log(a, 10)*b) + 1 )