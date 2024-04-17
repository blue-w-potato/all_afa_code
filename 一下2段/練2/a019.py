a,b=map(int,input().split())
s = 0
if b in [2,5,8]:s=200
elif a%2==1:s=100
elif a==b:s=50
print(s)