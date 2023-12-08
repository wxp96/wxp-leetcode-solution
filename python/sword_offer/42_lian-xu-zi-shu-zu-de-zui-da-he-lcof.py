from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre=0
        max_sum=-float('inf')
        for num in nums:
            if pre<0:
                pre=num
            else:
                pre+=num
            max_sum=max(pre,max_sum)
        return max_sum