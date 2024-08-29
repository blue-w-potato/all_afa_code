a = input()
if ' ' in a:
    print( (lambda x,y: x*y)( *map(int,a.split()) ) )
else:
    print(int(a)*int(input()))