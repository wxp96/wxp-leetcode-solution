from typing import List
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>dp[-1]:
                dp.append(nums[i])
            else:
                j=bisect.bisect_left(dp,nums[i])
                dp[j]=nums[i]
        return len(dp)