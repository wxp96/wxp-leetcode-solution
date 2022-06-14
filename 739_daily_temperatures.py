from typing import List
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for index, x in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < x:
                tIndex = stack.pop()
                res[tIndex] = index - tIndex
            stack.append(index)
        return res
                