from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        max_length=0
        for num in nums:
            cur=0
            if num in s:
                s.remove(num)
                cur+=1
            num+=1
            while num in s:
                cur+=1
                s.remove(num)
                num+=1
            max_length=max(max_length,cur)
        return max_length
    
s=Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
