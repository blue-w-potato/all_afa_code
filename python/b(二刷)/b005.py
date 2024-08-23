a = list(map(int,input().split()))
m = [0, 0]
for i in list(set(a)):
    if a.count(i)>m[1]:
        m = [ i, a.count(i) ]
print( *m )