a = int(input())
print('YES' if a%400==0 or a%100!=0 and a%4==0 else 'NO')