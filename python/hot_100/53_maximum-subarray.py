from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre=0
        res=[0]*len(nums)
        for i in range(len(nums)):
            res[i]=max(pre+nums[i],nums[i])
            pre=res[i]
        return max(res)