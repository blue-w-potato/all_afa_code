a,b = map(int,input().split())
c = [i for i in range(min(a,b),max(a,b)+1)]
print('+'.join(list(map(str,c[::-1 if a>b else 1]))),end='=')
print(sum(c))