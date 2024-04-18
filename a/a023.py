a = int(input())
ru = [a]
while ru[-1]!=1:
    ru.append(ru[-1]*3+1 if ru[-1]%2==1 else ru[-1]//2)
print(len(ru))