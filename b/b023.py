t = int(input())
rings = [ [  ] , [ i for i in range(t, 0, -1) ] , [  ] , [  ]]
while len(rings[1]) > 0:
    w = len(rings[3]) + (len(rings[3])==0)
    rings[2] += rings[3]
    rings[3] = []
    print( f'Ring {rings[1][-1]} from 1 to 3' )
    rings[3].append(rings[1].pop(-1))
    rings[1] += rings[2]
    rings[2] = []
    print( f'Ring {rings[1][-1]} from 1 to 2' )
    rings[2].append(rings[1].pop(-1))
    print( f'Ring {rings[3][-1]} from 3 to 2' )
    rings[2].append(rings[3].pop(-1))
    rings[2] += rings[1][w*-1:]
    rings[1] = rings[1][:w*-1]
    print( f'Ring {rings[1][-1]} from 1 to 3' )
    rings[3].append(rings[1].pop(-1))
    rings[3] += rings[2][w*-1:]
    rings[2] = rings[2][:w*-1]
    print( f'Ring {rings[2][-1]} from 2 to 1' )
    rings[1].append(rings[2].pop(-1))
    rings[1] += rings[3][w*-1:]
    rings[3] = rings[3][:w*-1]
    print( f'Ring {rings[2][-1]} from 2 to 3' )
    rings[3].append(rings[2].pop(-1))
    rings[2] += rings[1][w*-1:]
    rings[1] = rings[1][:w*-1]
    print( f'Ring {rings[1][-1]} from 1 to 3' )
    rings[3].append(rings[1].pop(-1))
    rings[3] += rings[2]
    rings[2] = []