# MemoryError

# 並查集-1
# n=int(input())
# sets = [ {i} for i in range(n) ]
# a=list(map(int,input().split()))
# for i in range(n):
#     sets[i] = sets[i]|sets[a[i]]
#     sets[a[i]] = sets[i]
#     for j in sets[i]:
#         sets[j] = sets[j]|sets[a[i]]
#         sets[a[i]] = sets[j]
#     for j in sets[a[i]]:
#         sets[j] = sets[j]|sets[i]
#         sets[i] = sets[j]
# s=0;e=1
# while s<len(sets)-1:
#     if len(sets[s]) == len(sets[s]&sets[e]):
#         sets.pop(e)
#     else:
#         e+=1
#     if e >= len(sets):
#         s+=1
#         e=s+1
# print(len(sets))

# 並查集-2
# n=int(input())
# a=list(map(int,input().split()))
# sets=[{i,a[i]} for i in range(n)]
# for i in range(n):
#     sets[i] = sets[i]|sets[a[i]]
#     sets[a[i]] = sets[i]
#     for k in sets[i]:
#         sets[a[i]] = sets[a[i]]|sets[k]
#         sets[k] = sets[a[i]]
#     for k in sets[a[i]]:
#         sets[i] = sets[i]|sets[k]
#         sets[k] = sets[i]
# s=0;e=1
# while s<len(sets)-1:
#     if len(sets[s])==len(sets[s]&sets[e]):
#         sets.pop(e)
#     else:
#         e+=1
#     if e>=len(sets):
#         s+=1
#         e=s+1
# print(len(sets))

# 圖形化-1
# 迭代次數過多
# n=int(input())
# a=list(map(int,input().split()))
# s=0;visited=[]
# def yee(node):
#     global a
#     global visited
#     global s
#     if node in visited:
#         s+=1
#         return
#     visited.append(node)
#     yee(a[node])
#     return
# for i in range(n):
#     if not(i in visited):
#         yee(i)
# print(s)

# 圖形化-2
# AC
n=int(input())
a=list(map(int,input().split()))
a={i:a[i] for i in a}
s=0;visited=set()

for i in range(n):
    if i in visited:
        continue
    k=i
    while not(k in visited):
        visited.add(k)
        k=a[k]
    s+=1
print(s)