a,b = map(lambda x:x[::-1],input().split())
s=0
for i in range(len(a)):
    if a[i]==b[i]:
        s+=1
    else:
        break
if s==8:print(20*10000)
if s==7:print(4*10000)
if s==6:print(10000)
if s==5:print(4*1000)
if s==4:print(1000)
if s==3:print(200)
if s<3:print(0)