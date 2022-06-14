from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        rs=float("inf")
        for idx in range(len(nums)-k+1):
            rs=min(rs,nums[idx+k-1]-nums[idx])
        return rs