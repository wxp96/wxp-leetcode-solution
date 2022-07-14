from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        pre=nums[0]
        for num in nums[1:]:
            if pre>0:
                pre+=num
            else:
                pre=num
            if pre>max_sum:
                max_sum=pre
        return max_sum