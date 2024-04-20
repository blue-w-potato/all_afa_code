a=int(input())
if a%6==1 or a%6==5:
    for i in range(5,int(a**0.5)+1):
        if a%i==0:
            print('NO')
            break
    else:
        print('YES')
else:
    print('NO')