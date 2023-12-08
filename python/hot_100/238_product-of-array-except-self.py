from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]*len(nums)
        for i in range(1,len(nums)):
            left[i]=left[i-1]*nums[i-1]
        right=1
        for i in reversed(range(len(nums))):
            left[i]=left[i]*right
            right=right*nums[i]
        return left
    
s=Solution()
print(s.productExceptSelf([-1,1,0,-3,3]))