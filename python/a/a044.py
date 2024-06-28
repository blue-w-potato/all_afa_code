a=int(input())
c=[]
d=[]
for i in range(1,int(a**0.5)+1):
    if a%i==0:
        c.append(i)
for i in c[1:]:
    d.append(a//i)
c=sum(c+d)
print('Perfect' if c==a else ('Abundant' if c>a else 'Deficient'))