# I(1)、V(5)、X(10)、L(50)、C(100)、D(500)、M(1000)

Dict = {
    'I' : 1,
    'IV' : 4,
    'V' : 5,
    'IX' : 9,

    'X' : 10,
    'XL' : 40,
    'L' : 50,
    'XC' : 90,

    'C' : 100,
    'CD' : 400,
    'D' : 500,
    'CM' : 900,

    'M' : 1000 
    }

def roman_num(string = '', roman = Dict ):
    if string == '' or string == None:
        return 0
    key_array = list( roman.keys() )
    value_array = list( roman.values() )
    num = 0
    x = 0
    y = 2
    while True:
        if x >= len(string) or y > len(string):
            if y == x + 2:
                y -= 1
                continue
            return num
        if string[x:y] in key_array:
            num += roman[key_array[key_array.index(string[x:y])]]
            x = y + 0
            y = x + 2
            continue
        y = x + 1

print(roman_num(input()))