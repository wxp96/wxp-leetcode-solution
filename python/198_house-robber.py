from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre=0
        for i in range(1,len(nums)):
            nums[i]=max(nums[i]+pre,nums[i-1])
            pre=nums[i-1]
        return nums[-1]