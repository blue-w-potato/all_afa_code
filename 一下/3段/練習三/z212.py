k = list(map(int,input().split()))
i=0
while i<len(k)-1:
    if k[i]==k[i+1]:
        k.pop(i)
    else:
        i+=1
s=0
for i in range(1,len(k)-1):
    if k[i-1]<k[i] and k[i]>k[i+1]:
        s+=1
print(s)