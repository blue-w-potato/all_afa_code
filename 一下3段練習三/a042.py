# for i in range(1, 11):
#     print(i, 13**i)
# print()
a = int(input())
s = ( 1, 6, 9, 6, 9,
      0, 1, 2, 7, 4,
      3, 8, 5, 8, 5,
      4, 3, 2, 7, 0)
print(s[a%20-1])