ru=list(map(int,input().split()[1:]))
weiru={}
for i in list(set(ru)):
    weiru[i]=0
for i in ru:
    weiru[i]+=1
k=[]
for i in weiru.keys():
    k.append([i,weiru[i]])
k.sort(key=lambda x:x[1],reverse=True)
print(*k[0])