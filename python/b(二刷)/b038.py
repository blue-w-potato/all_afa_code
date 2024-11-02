n = int(input())
chars = [ str(i) for i in range(1, n+1) ]
def backTracking( long, ans, chars ):
    if len(ans) == long:
        print( ans )
        return
    for i in chars:
        newChars = chars.copy()
        newChars.remove(i)
        backTracking( long, ans+i, newChars )
    return
backTracking( n, '', chars )