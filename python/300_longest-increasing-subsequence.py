from typing import List
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         res=[]
#         for i in range(len(nums)):
#             if not res or nums[i]>res[-1]:
#                 res.append(nums[i])
#             else:
#                 l,r=0,len(res)
#                 while l<r:
#                     mid=l+(r-l)//2
#                     if res[mid]<nums[i]:
#                         l=mid+1
#                     elif res[mid]>nums[i]:
#                         r=mid
#                     else:
#                         r=mid
#                 res[l]=nums[i]
#         return len(res)
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res=[]
        for i in range(len(nums)):
            if not res or nums[i]>res[-1]:
                res.append(nums[i])
            else:
                pos=bisect.bisect_left(res,nums[i])
                res[pos]=nums[i]
        return len(res)

s=Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))