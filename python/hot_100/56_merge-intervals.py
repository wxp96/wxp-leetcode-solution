from typing import List
from collections import deque
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x:(x[1],x[0]))
        stack=deque()
        for x,y in intervals:
            while stack and x<=stack[-1][1]:
                pre=stack.pop()
                x=min(x,pre[0])
                y=max(y,pre[1])
            stack.append([x,y])
        return list(stack)
