a=13
for i in range(int(input())-1):
    a=a*13%1000
print(a%100//10)