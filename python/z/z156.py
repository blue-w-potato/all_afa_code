for _ in range(int(input())):
    a = input()
    print(f'Sum of all digits of {a} is {sum(list(map(int,list(a))))}')