from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=nums[0]
        cnt=0
        for i in range(len(nums)):
            if cnt==0:
                candidate=nums[i]
            if candidate==nums[i]:
                cnt+=1
            else:
                cnt-=1
        return candidate