# 分數<=30的*1.6，若30~50的部份*1.2，若50~70的部份*0.8，若70~100的部份*0.4
nums = list(map( eval, input().split(',') ))
for num in nums:
    score = 0
    if num <= 30:
        score = num*1.6
    elif num < 50:
        score = 30 * 1.6 + ( num-30 ) * 1.2
    elif num < 70:
        score = 30 * 1.6 + 20 * 1.2 + ( num-50 ) * 0.8
    else:
        score = 30 * 1.6 + 20 * 1.2 + 20 * 0.8 + ( num-70 ) * 0.4
    print(f'{score:.1f}', end=' ')