def remove_not_num( string ):
    array = list(string)
    i = 0
    while i<len(array):
        if array[i] in '0123456789':
            i+=1
        else:
            array.remove(array[i])
    return int(''.join(array))

print(sum([remove_not_num(input()) for i in range(3)]))