n = list(map(int,list(input())))
print(10-sum([ (i+1)*n[i] for i in range(len(n)) ])%10 if sum([ (i+1)*n[i] for i in range(len(n)) ])%10  else 0)