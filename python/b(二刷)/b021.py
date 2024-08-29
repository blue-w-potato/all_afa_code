n = int(input())
data = [ list(map( int, input().split() )) for i in range(n) ]
a = [[ i[0], sum(i[1:]), i[3] ] for i in data ]
a.sort( key=lambda x:x[2], reverse=True )
a.sort( key=lambda x:x[1], reverse=True )
for i in a:
    print(i[0])