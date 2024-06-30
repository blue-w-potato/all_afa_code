a,b,c=eval(input()),eval(input()),eval(input())
k = b**2-4*a*c
if k<0:
    print("Your equation has no root.")
elif k==0:
    print(b*-1/(2*a))
else:
    print((b*-1+k**0.5)/(2*a),end=', ')
    print((b*-1-k**0.5)/(2*a))