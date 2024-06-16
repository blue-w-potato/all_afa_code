d,f=0,0
for i in range(10):
    if int(input())%2==0:
        d+=1
    else:
        f+=1
print(f'''Even numbers: {d}
Odd numbers: {f}''')