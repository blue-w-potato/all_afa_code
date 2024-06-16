pizza = {6:float(f'{3*3*3.1415926:.4f}'),
         9:float(f'{4.5*4.5*3.1415926:.4f}'),
         12:float(f'{6*6*3.1415926:.4f}'),
         16:float(f'{8*8*3.1415926:.4f}'),
         20:float(f'{10*10*3.1415926:.4f}')}
while 1:
    try:
        a=list(map(lambda x: pizza[int(x)],input().split()[1:]))
        b=list(map(lambda x: pizza[int(x)],input().split()[1:]))
        print(f'{abs(sum(b)-sum(a)):.2f}')
    except:
        break
