k = [0, 1]
for i in range(int(input())):
    if i<len(k):
        print(k[i], end=' ')
    else:
        k.append(k[-1]+k[-2])
        print(k[-1], end=' ')