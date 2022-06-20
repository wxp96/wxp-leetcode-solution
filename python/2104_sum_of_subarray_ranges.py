from typing import List
from collections import deque
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def pop_deque(s,num,b):
            if b:
                while s and s[-1]<num:
                    s.pop()
            else:
                while s and s[-1]>num:
                    s.pop()
            s.append(num)

        i=2
        rs=0
        while i<=len(nums):
            s1=deque()
            s2=deque()
            for x in range(i-1):
                pop_deque(s1,nums[x],True)
                pop_deque(s2,nums[x],False)
            for j in range(i-1,len(nums)):
                pop_deque(s1,nums[j],True)
                pop_deque(s2,nums[j],False)
                max_n=s1[0]
                min_n=s2[0]
                rs+=(max_n-min_n)
                if s1[0]==nums[j-i+1]:
                    s1.popleft()
                if s2[0]==nums[j-i+1]:
                    s2.popleft()
            i+=1
        return rs

s=Solution()
print(s.subArrayRanges([4,-2,-3,4,1]))