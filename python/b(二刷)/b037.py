n, m = map(int, input().split())
chars = [ str(i) for i in range(m+1) ]
def backTracking( long, ans, chars ):
    if len(ans) == long:
        print( ans )
        return
    for i in chars:
        backTracking( long, ans+i, chars )
    return
backTracking( n, '', chars )