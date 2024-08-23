a = list(input())
for i in a:
    print( chr( ord(i)-2 + (ord(i)-2 < 65)*26 ), end = "" )