a,b=map(int,input().split())
c=1
for i in range(1,int(min(a,b))+1):
    if a%i==b%i==0:
        c=i
print(c)