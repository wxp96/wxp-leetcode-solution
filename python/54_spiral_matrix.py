from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        res+=list(matrix.pop(0))
        while matrix:
            matrix=list(zip(*matrix))
            matrix=matrix[::-1]
            res+=list(matrix.pop(0))
        return res

s=Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
