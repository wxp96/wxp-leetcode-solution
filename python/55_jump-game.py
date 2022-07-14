from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        max_now=nums[0]
        i=1
        while i<len(nums)-1 and i<max_now:
            max_now=max(max_now,i+nums[i])
            if max_now>=len(nums)-1:
                return True
            i+=1
        return False

s=Solution()
print(s.canJump([2,3,1,1,4]))