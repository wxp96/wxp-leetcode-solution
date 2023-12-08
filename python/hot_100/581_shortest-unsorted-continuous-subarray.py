from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        min_num=float('inf')
        left=-1
        n=len(nums)
        for i in range(n-1,-1,-1):
            if nums[i]>min_num:
                left=i
            else:
                min_num=nums[i]
        max_num=-float('inf')
        right=-1
        for i in range(n):
            if nums[i]<max_num:
                right=i
            else:
                max_num=nums[i]
        return 0 if right==-1 else right-left+1