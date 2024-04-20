for i in range(int(input())):
    a,b=map(int,input().split())
    if a==b:
        print(f'Case {i+1}:',0)
    else:
        print(f'Case {i+1}:','A'if a>b else 'B', max(a,b)-min(a,b))