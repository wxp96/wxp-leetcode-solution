from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        pre_p=0
        pre=nums[0]
        for i in range(1,len(nums)-1):
            cur=max(pre_p+nums[i],pre)
            pre_p,pre=pre,cur
        last_p=cur
        pre_p=0
        pre=nums[1]
        for i in range(2,len(nums)):
            cur=max(pre_p+nums[i],pre)
            pre_p,pre=pre,cur
        last=cur
        return max(last,last_p)

s=Solution()
print(s.rob([2,3,2]))