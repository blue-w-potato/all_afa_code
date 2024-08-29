# 假裝 python 沒有自帶大數計算

d = input()
if ' ' in d:
    d = d.split()
else:
    d = [ d, input() ]
a = [ list(map( int, list(i) )) for i in d ]
a,b = a
a.reverse(); b.reverse()
c = ''
n=0
if len(a) > len(b): a,b = b,a
for i in range(len(b)):
    s = b[i] + n
    if i<len(a):
        s+=a[i]
    n = s//10
    c = str(s)[-1] + c
if n>0:print(n, end='')
print(c)
