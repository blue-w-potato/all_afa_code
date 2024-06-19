while 1:
    a = eval(input())
    if a == -9999:break
    b = eval(input())
    if b == -9999:break
    bmi = b/((a/100)**2)
    print(f'BMI: {bmi:.2f}')
    print('State: ',end='')
    if bmi<18.5:print('under weight')
    elif bmi<25:print('normal')
    elif bmi<30:print('over weight')
    else:print('fat')