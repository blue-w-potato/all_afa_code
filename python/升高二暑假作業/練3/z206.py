a,b = 0,0
for i in range(10):
    if int(input())%2:b+=1
    else:a+=1
print(f'''Even numbers: {a}
Odd numbers: {b}''')