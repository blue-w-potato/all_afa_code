c = [10000, 5000, 1000, 500, 100, 50, 10, 5]
n = int(input())
s = 0
for i in c:
    if n>=i:
        s+=n//i
        n-=i*(n//i)
print(s+n)