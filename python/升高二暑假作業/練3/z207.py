a,b,c = 0,0,0
for i in range(5):
    n = int(input())
    if n==1:a+=1
    elif n==2:b+=1
    else:c+=1
    print(f'''Total votes of No.1: Nami =   {a}
Total votes of No.2: Chopper =   {b}
Total null votes =   =   {c}''')
if a<b:print('=> No.2 Chopper won the election.')
elif a>b:print('=> No.1 Nami won the election.')
else:print('=> No one won the election.')