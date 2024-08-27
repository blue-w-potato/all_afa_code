
a = float(input())
b = float(input())
bmi = a/(b**2/10000)
print( (bmi+(0.01)*((bmi*100%1)>=(0.5)))*100//1/100  )
if bmi < 18.5:print('light')
elif 18.5 <= bmi < 24:print('normal')
else:print('heavy')