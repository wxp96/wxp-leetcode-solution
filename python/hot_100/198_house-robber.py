from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        ahead,ahead2=0,0
        for i in range(len(nums)):
            cur=max(ahead2+nums[i],ahead)
            ahead2=ahead
            ahead=cur
        return ahead