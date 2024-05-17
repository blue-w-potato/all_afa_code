for i in range(int(input())):
    a,b = map(int,input().split())
    print( f'Case {i+1}: ' + ('0' if a==b else( 'A' if a>b else 'B' )+ ' ' + str(abs(a-b)) ) )