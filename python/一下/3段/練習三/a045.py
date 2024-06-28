a = int(input())
if a in ( 2, 3, 5, 7 ):
    print('YES')
elif a % 6 in ( 1, 5 ):
    for i in range( 5, int(a**0.5)+1 ):
        if a%i == 0:
            print('NO')
            break
    else:
        print('YES')
else:
    print('NO')