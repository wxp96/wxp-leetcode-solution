from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        diff=sum(nums)-target
        if diff<0 or diff%2:
            return 0
        neg=diff//2
        memo=[0 for i in range(neg+1)]
        memo[0]=1
        for i in range(len(nums)):
            for j in range(neg,-1,-1):
                if j-nums[i]>=0:
                    memo[j]=memo[j]+memo[j-nums[i]]
        return memo[-1]