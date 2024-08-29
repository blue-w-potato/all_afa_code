a = input()
if ' ' in a:
    print( sum( map(int, a.split()) ) )
else:
    print( int(a) + int(input()) )