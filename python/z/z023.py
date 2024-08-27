# 「恭喜你猜對了 !」、「猜的數字太小了」、或「猜的數字太大了
a = int(input())
if a==7:print('恭喜你猜對了 !')
elif a<7:print('猜的數字太小了')
else:print('猜的數字太大了')