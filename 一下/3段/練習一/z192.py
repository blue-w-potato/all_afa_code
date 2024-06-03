n = int(input())
inpu = list(map(int,input().split()))
a = inpu[::2]; b = inpu[1::2]
x,y = map(int,input().split())
s = sum([ b[i] for i in range(n//2) if x<=a[i]<=y ])
print(s)