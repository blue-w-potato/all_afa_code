a,b=map(int,input().split())
s = 0
if b in [2,5,8]:s+=200
if a%2==1:s+=100
if a==b:s+=50
print(s)