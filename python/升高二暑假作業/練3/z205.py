while 1:
    n = int(input())
    if n==-9999:break
    print( f'{n} is a leap year.' if n%400==0 or n%100!=0 and n%4==0 else f'{n} is not a leap year.' )