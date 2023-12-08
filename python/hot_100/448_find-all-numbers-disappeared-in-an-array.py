from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i,num in enumerate(nums):
            x=(num-1)%n
            nums[x]+=n

        res=[i+1 for i,x in enumerate(nums) if x<=n]
        return res