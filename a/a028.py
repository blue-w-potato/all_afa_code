def ru(n):
    if n==2:
        return 2
    return n*ru(n-1)
a,b = map(int,input().split())
print(ru(a)//ru(a-b))