from math import log
a,b = map(int,input().split())
f = lambda x: True if x ==10 else ( x//10 if x%10 == 0 else False )
if a == 1 or b == 0:  
    print(1)
elif a == 0:
    print(0)
elif a == 10:
    print(b+1)
elif f(a):
    print((len(str(a))-1)*b+1)
elif b == 1:
    print(len(str(a)))
else:
    print( int(log(a, 10)*b) + 1 )