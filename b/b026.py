a = list(map(int,input().split()))
a[0] = 0
for i in range(1,len(a)):
    a[i]+=a[i-1]
n=max(a)
if n>0:
    print(n)
else:
    print(0)