while 1:
    a = float(input())
    if a==-9999:break
    b = float(input())
    if b==-9999:break
    bmi = b/(a**2/10000)
    print('BMI:',f'{bmi*100//1/100 + (bmi*100%1>=0.5)*0.01:.2f}')
    print('State: ',end='')
    if bmi < 18.5:print('under weight')
    elif 18.5 <= bmi < 25:print('normal')
    elif 25.0 <= bmi < 30:print('over weight')
    elif 30 <= bmi:print('fat')