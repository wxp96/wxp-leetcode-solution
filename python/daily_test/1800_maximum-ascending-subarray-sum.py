from typing import List
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum=cur=nums[0]
        for i in range(len(nums)):
            if nums[i]<nums[i-1] or i==len(nums)-1:
                max_sum=max(max_sum,cur)
                cur=nums[i]
            else:
                cur+=max_sum
        return max_sum
