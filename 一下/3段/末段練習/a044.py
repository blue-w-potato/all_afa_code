k = []
n = int(input())
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        k.append(i)
s=len(k)
for i in k[:s]:
    k.append(n//i)
k = sum(list(set(k)))-n
if k==n:
    print('Perfect')
elif k>n:print('Abundant')
else:print('Deficient')