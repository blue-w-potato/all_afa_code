a,b = map(int,input().split())
print(f'{a}={b}' if a==b else (f'{a}>{b}' if a>b else f'{a}<{b}'))