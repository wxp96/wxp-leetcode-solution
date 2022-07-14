from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        @lru_cache(None)
        def dp(l,r):
            if l>=r-2:
                return 0
            res=0
            for i in range(l+1,r-1):
                cur=nums[l]*nums[r-1]*nums[i]
                res=max(res,cur+dp(l,i+1)+dp(i,r))
            return res
        nums=[1]+nums+[1]
        return dp(0,len(nums))

s=Solution()
print(s.maxCoins([3,1,5,8]))