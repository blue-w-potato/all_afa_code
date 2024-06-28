n=int(input())
if n%3:
    if n%5:
        print(n,'is not a multiple of 3 or 5.')
    else:
        print(n, 'is a multiple of 5.')
else:
    if n%5:
        print(n,'is a multiple of 3.')
    else:
        print(n, 'is a multiple of 3 and 5.')
    