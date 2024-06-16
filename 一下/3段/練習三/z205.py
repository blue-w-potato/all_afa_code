while 1:
    a=int(input())
    if a == -9999:
        break
    print(f'{a}','is a leap year.' if a%400==0 or a%100!=0 and a%4==0 else 'is not a leap year.')