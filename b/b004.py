# 一開始有兩個正整數 N、M (0<=M<N<=20)，N 代表收容人的人數(編號從 1 到 N)，M 代表回來的人數，接下來有 M 個正整數，分別代表這 M 位已經回來的收容人編號(不用考慮編號超出範圍或其他錯誤)。
ru=list(map(int,input().split()))
noback=[i for i in range(1,1+ru[0])]
for i in ru[2:]:
    noback.remove(i)
print(*noback)