from typing import List
from collections import deque
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=deque()
        res=[-1]*len(nums)
        for i in range(2*len(nums)-1,0,-1):
            while stack and nums[i%len(nums)]>=stack[-1]:
                stack.pop()
            if stack:
                res[i%len(nums)]=stack[-1]
            stack.append(nums[i%len(nums)])