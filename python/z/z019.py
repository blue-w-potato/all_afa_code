
a = float(input())
b = float(input())
bmi = a/(b**2/10000)
print( (bmi+(0.01)*((bmi*100%1)>=(0.5)))*100//1/100  )