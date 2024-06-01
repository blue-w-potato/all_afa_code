a = eval(input())
b = eval(input())
nums = [[]]
for i in range(a,b+1):
    if i%4 == 0 or i%9 == 0:
        nums[-1].append(i)
        if len(nums[-1]) == 10:
            nums.append([])
for i in nums:
    for j in i:
        print(f'{j:<4}', end='')
    print()
s = []
for i in nums:s+=i
print(len(s))
print(sum(s))