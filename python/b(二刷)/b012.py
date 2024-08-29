roman = {'I':1,
         'V':5,
         'X':10,
         'L':50,
         'C':100,
         'D':500,
         'M':1000}

a = list( input() )
num_a = [ roman[i] for i in a ]
s = 0
for i in range(len(num_a)-1):
    if num_a[i] >= num_a[i+1]:
        s += num_a[i]
    else:
        s -= num_a[i]
s += num_a[-1]


print(s)