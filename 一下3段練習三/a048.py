n = int(input())
for i in range(1,n+1):
    print( "_"*(n-i) + str(i)*(1+(i-1)*2) )