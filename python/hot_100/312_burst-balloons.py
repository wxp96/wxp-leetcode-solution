from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # memo[i][j]=max(memo[i][k]+nums[i]*nums[k]*nums[j]+memo[k][j])
        nums.append(1)
        nums.insert(0,1)
        memo=[[0]*len(nums) for i in range(len(nums))]
        for i in range(2,len(nums)):
            for j in range(len(nums)):
                if i+j>=len(nums):
                    break
                for k in range(j+1,i+j):
                    memo[j][i+j]=max(memo[j][i+j],memo[j][k]+nums[j]*nums[k]*nums[i+j]+memo[k][i+j])
        return memo[0][len(nums)-1]