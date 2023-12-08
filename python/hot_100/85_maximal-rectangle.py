from typing import List
from collections import deque
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def largestRectangleArea(heights: List[int]) -> int:
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

        ans=0
        memo=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='1':
                    memo[i][j]=1 if i==0 else memo[i-1][j]+1
        print(memo)
        for i in range(len(memo)):
            ans=max(ans,largestRectangleArea(memo[i]))
        return ans

s=Solution()
print(s.maximalRectangle([["1","0"],["1","0"]]))