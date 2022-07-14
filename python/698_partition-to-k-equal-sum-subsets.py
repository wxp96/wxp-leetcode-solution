from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_sum=sum(nums)
        if nums_sum%k:
            return False
        mean_sum=nums_sum//k
        for 