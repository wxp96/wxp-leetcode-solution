from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2:
            return False
        half=total//2
        memo=[False]*(half+1)
        memo[0]=True
        for i in range(1,len(nums)+1):
            for j in range(half,0,-1):
                if j>=nums[i-1]:
                    memo[j]=memo[j] or memo[j-nums[i-1]]
        return memo[-1]
    
s=Solution()
print(s.canPartition([1,2,5]))