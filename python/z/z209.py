for _ in range(int(input())):
    a=list(map(int,input().split(',')))
    b=list(map(int,input().split(',')))
    print(len([i for i in a if i in b]))