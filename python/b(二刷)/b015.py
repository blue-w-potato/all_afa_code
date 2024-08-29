for i in range(3):
    a=input().split()
    if 'BILL' in a:
        print( i+1, a.index('BILL')+1 )
        break
else:
    print('NO')