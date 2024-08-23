a = int(input())
b = int(input())
s,n = 0,0
c = 0
for i in range(a,b+1):
    if i%9 and i%4:continue
    print(f'{i:<4}',end='')
    c+=1
    if c==10:
        c=0
        print()
    s+=i
    n+=1
if c>0:print()
print(n)
print(s)
