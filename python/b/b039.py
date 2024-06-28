

import time
s=time.time()
#AC
m = int(input())
def yee( array, t0, t1, t2, row ):
    global m
    # print(array, 'a')
    # print(row,'r')
    # for i in table:print(i)
    if row == m:
        if len(array) == m:
            for i in array:
                print(i+1, end=' ')
            print()
        return
    for i in range( m ):
        if not(t1[i+row] and t2[row-i] and t0[i]):
            continue
        t0[i] = 0
        t1[i+row] = 0
        t2[row-i] = 0
        yee( array+[i], t0, t1, t2, row+1 )
        t0[i] = 1
        t1[i+row] = 1
        t2[row-i] = 1
k = [1 for i in range((m-1)*2+1)]
yee([], k[:m], k[:], k[:], 0)


print(time.time()-s)





# 目前最快
# import time
# s=time.time()

# m = int(input())
# def yee( array, table ):
#     global m
#     # print(array, 'a')
#     # print(row,'r')
#     # for i in table:print(i)
#     if not table:
#         if len(array) == m:
#             for i in array:
#                 print(i+1, end=' ')
#             print()
#         return
#     while 1 in table[0]:
#         i = table[0].index(1)
#         if i in array:
#             table[0][i]=0
#             continue
#         k = [ o[:] for o in table ]
#         for j in range( 1, len(k) ):
#             if i+j <m:
#                 k[j][i+j] = 0
#                 if -1<i-j:
#                     k[j][i-j] = 0
#             elif -1<i-j:
#                 k[j][i-j] = 0
#                 if i+j <m:
#                     k[j][i+j] = 0
#             else:
#                 break
#         yee( array+[i], k[1:] )
#         table[0][i]=0
        
        
# yee([],  [[1 for i in range(m)] for j in range(m)])

# print(time.time()-s)

# 後來試試看鏈結串列
# import time
# s=time.time()

# m = int(input())
# class linked_list():
#     def __init__( self, value, next  ):
#         self.value = value
#         self.next = next
#     def append( self, new ):
#         if self.next == None:
#             return linked_list( self.value, linked_list(new+1, None) )
#         return linked_list( self.value, self.next.append(new) )
#     def print( self ):
#         print(self.value, end=' ')
#         if self.next:
#             self.next.print()
#         else:
#             print()
# def yee( array, table ):
#     # array.print()
#     # for o in table:print(o)
#     if not table:
#         if array:array.next.print()
#         return
#     while 1 in table[0]:
#         i = table[0].index(1)
#         # k = [ o[:] for o in table ]
#         # for j in range( 1, s):
#         #     if i+j <m:
#         #         k[j][i+j] = 0
#         #         if -1<i-j:
#         #             k[j][i-j] = 0
#         #     elif -1<i-j:
#         #         k[j][i-j] = 0
#         #         if i+j <m:
#         #             k[j][i+j] = 0
#         #     else:
#         #         break
#         k = []
#         for j in range(1, len(table) ):
#             k.append([])
#             for jj in range(m):
#                 if jj+j == i or jj-j == i or jj == i:
#                     k[-1].append(0)
#                 else:
#                     k[-1].append(table[j][jj])
#         yee( array.append(i), k )
#         table[0][i] = 0
        
        
# yee(linked_list('', None),  [[1 for i in range(m)] for j in range(m)])

# print(time.time()-s)

# 舊的
# import time
# s=time.time()

# m = int(input())
# def yee( array, table ):
#     # print(array,'a')
#     # for o in table:print(o)
#     if not table:
#         if len(array) == m:
#             for i in array:
#                 print(i+1, end=' ')
#             print()
#         return
#     s = len(table) 
#     while 1 in table[0]:
#         i = table[0].index(1)
#         if i in array:
#             table[0][i]=0
#             continue
#         # k = [ o[:] for o in table ]
#         # for j in range( 1, s):
#         #     if i+j <m:
#         #         k[j][i+j] = 0
#         #         if -1<i-j:
#         #             k[j][i-j] = 0
#         #     elif -1<i-j:
#         #         k[j][i-j] = 0
#         #         if i+j <m:
#         #             k[j][i+j] = 0
#         #     else:
#         #         break
#         k = []
#         for j in range(1, s):
#             k.append([])
#             for jj in range(m):
#                 if jj+j == i or jj-j == i:
#                     k[-1].append(0)
#                 else:
#                     k[-1].append(table[j][jj])
#         yee( array+[i], k )
#         table[0][i]=0
        
        
# yee([],  [[1 for i in range(m)] for j in range(m)])
# print(time.time()-s)


