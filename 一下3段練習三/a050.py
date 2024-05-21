n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        print(f'{j}x{i}={j*i:>2}',end="  ")
    print()