# from typing import List
# class Solution:
#     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
#         amount=sum(nums)
#         if amount%k:
#             return False
#         dp_table=[[True]+[False]*amount for i in range(len(nums)+1)]
#         for i in range(1,len(nums)+1):
#             for j in range(1,amount+1):
#                 if j-nums[i-1]<0:
#                     dp_table[i][j]=dp_table[i-1][j]
#                 else:
#                     dp_table[i][j]=dp_table[i-1][j] or dp_table[i-1][j-nums[i-1]]
#         res=True
#         per=int(amount/k)
#         point=1
#         for i in range(k):
#             point+=per
#             res=res and dp_table[point]
#         return res

# s=Solution()
# print(s.canPartitionKSubsets([2,2,2,2,3,4,5],4))