from typing import List
from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=deque()
        d=dict()
        for num in nums2[::-1]:
            while len(stack)!=0 and stack[-1]<=num:
                stack.pop()
            if len(stack)!=0:
                d[num]=stack[-1]
            else:
                d[num]=-1
            stack.append(num)
        res=[d[i] for i in nums1]
        return res