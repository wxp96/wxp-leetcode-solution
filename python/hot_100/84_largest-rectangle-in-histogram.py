from typing import List
from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=deque()
        stack_idx=deque([-1])
        max_area=0
        for i in range(len(heights)):
            while stack and heights[i]<stack[-1]:
                h=stack.pop()
                stack_idx.pop()
                idx=stack_idx[-1]
                max_area=max(max_area,h*(i-idx-1))
            stack.append(heights[i])
            stack_idx.append(i)
        while stack:
            h=stack.pop()
            stack_idx.pop()
            idx=stack_idx[-1]
            max_area=max(max_area,h*(len(heights)-1-idx))
        return max_area

s=Solution()
print(s.largestRectangleArea([2,1,5,6,2]))