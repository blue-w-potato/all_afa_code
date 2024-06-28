a = [ input().split() for i in range(3) ]
b = 1
for i in range(3):
    for j in range(len(a[i])):
        if a[i][j].upper() == 'BILL':
            print(i+1, j+1)
            b = 0
            break
if b:
    print('NO')