from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=-float('inf')
        max_fin=1
        min_fin=1
        for i in range(len(nums)):
            max_fin1=max(nums[i],nums[i]*max_fin,nums[i]*min_fin)
            min_fin1=min(nums[i],nums[i]*max_fin,nums[i]*min_fin)
            max_fin=max_fin1
            min_fin=min_fin1
            res=max(max_fin,res)
        return res
    
s=Solution()
print(s.maxProduct([-2,3,-4]))