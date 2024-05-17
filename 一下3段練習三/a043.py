a,b = map(int,input().split())
if a<b:
    a,b=b,a
while a%b!=0:
    a%=b
    if a<b:
        a,b=b,a
print(b)