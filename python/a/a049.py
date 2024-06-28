a=int(input())
b='@--'*a
if a==1:
    print('@')
for i in range(0,a):
    print(f'{b}'[3-i%3:3-i%3+a])