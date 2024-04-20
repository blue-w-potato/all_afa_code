a=int(input())
ru = [i for i in range(1,a+1)]
for i in range(1,a+1):
    for j in ru:
        print(f'{j}x{i}={i*j:2}',end='  ')
    print()