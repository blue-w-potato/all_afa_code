a,b = map(int,input().split())
if b>a:
    s = [ str(i) for i in range(a,b+1) ]
else:
    s = [ str(i) for i in range(a,b-1,-1) ]
    
print('+'.join(s)+f'={sum(list(map(int,s)))}')