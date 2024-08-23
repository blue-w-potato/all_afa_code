n = int(input())
print('   1')
for i in range(2,n+1):
    for j in range(1,i+1):
        print(f'{i*j:>4}',end='')
    print()