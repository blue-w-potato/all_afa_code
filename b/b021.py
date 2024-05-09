k = [[i+1, list(map(int,input().split()[1:]))] for i in range(int(input()))]
k.sort(key=lambda x:x[1][2], reverse=True)
k.sort(key=lambda x:sum(x[1]), reverse=True)
for i in k:
    print(i[0])