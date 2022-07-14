from typing import List
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo=[[[0,0] for j in range(len(nums))] for i in range(len(nums))]
        for i in range(len(nums)):
            memo[i][i][0]=nums[i]
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                left=memo[i+1][j][1]+nums[i]
                right=memo[i][j-1][1]+nums[j]
                if left>right:
                    memo[i][j][0]=left
                    memo[i][j][1]=memo[i+1][j][0]
                else:
                    memo[i][j][0]=right
                    memo[i][j][1]=memo[i][j-1][0]
        fir,sec=memo[0][len(nums)-1]
        return fir>=sec

s=Solution()
print(s.PredictTheWinner([1,5,2]))