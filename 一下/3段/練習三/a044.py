a = int(input())
s = [1]
for i in range(2, a//2+1):
    if a%i == 0:
        s.append(i)
        s.append(a//i)
s = list(set(s))
# s.sort()
# print(s)
if sum(s)>a:
    print('Abundant')
elif sum(s)==a:
    print('Perfect')
else:
    print('Deficient')