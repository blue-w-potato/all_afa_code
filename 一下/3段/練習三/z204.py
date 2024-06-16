while 1:
    a=eval(input())
    if a == -9999:
        break
    b=eval(input())
    if b == -9999:
        break
    
    bmi = b/((a*0.01)**2)
    print(f'BMI: {bmi:.2f}')
    # BMI < 18.5                 under weight
    # 18.5 <= BMI < 25       normal
    # 25.0 <= BMI < 30      over weight
    # 30 <= BMI                 fat
    e=''
    if bmi<18.5:e='under weight'
    elif bmi<25:e='normal'
    elif bmi<30:e='over weight'
    else:e='fat'
    print('State:',e)