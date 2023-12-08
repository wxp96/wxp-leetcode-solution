# import sys 
# def func(arr):
#     def backtrack(i,j):
#         n=1
#         while True:
#             for a in range(1,n+1):
#                 if i+n>=len(arr) or j+a>=len(arr[0]) or arr[i+n][j+a]=='0' or arr[i+a][j+n]=='0':
#                     return n**2
#             n+=1
#     res=1
#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             if arr[i][j]=='1':
#                 res=max(res,backtrack(i,j))
#     return res

# print(func([["0","1","1","1"],["1","0","1","1"]]))