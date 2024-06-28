a=int(input())
b=int(input())
if a>b:a,b=b,a
for i in range(a+1,b+1):
    a+=i
print(a)