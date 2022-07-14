from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        max_now=max_next=0
        res=0
        for i in range(len(nums)):
            
            if max_next>=len(nums)-1:
                return res+1
            if i>max_now:
                res+=1
                max_now=max_next
            max_next=max(i+nums[i],max_next)

s=Solution()
print(s.jump([2,3,1,1,4]))
