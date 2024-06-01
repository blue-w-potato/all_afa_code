while 1:
    n = eval(input())
    if n == -9999:break
    # 90 ~ 100    A
    if n > 89:
        print('A')
    elif n>79:
        print('B')
    elif n>69:
        print('C')
    elif n>59:
        print('D')
    else:
        print('E')
    # 80 ~ 89 B
    # 70 ~ 79 C
    # 60 ~ 69 D
    # 0 ~ 59  E