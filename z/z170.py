from math import gcd


while 1:
    try:
        a,b,x,y,w=input().split()
        a,b,x,y=map(int,[a,b,x,y])
        if w in '+-':
            e=a*y+x*b if w=='+' else a*y-x*b
            h=y*b
        else:
            if w=='/':
                x,y=y,x
            e=a*x
            h=b*y
        if e>0 and h<0 or e<0 and h<0:
            e*=-1
            h*=-1
        if e%h==0:
            print(e//h)
        else:
            k=gcd(e,h)
            e//=k
            h//=k
            print(f'{e}/{h}')
        
    except:
        break