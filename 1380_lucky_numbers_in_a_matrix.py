from typing import List
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_s=set()
        rs=[]
        for row in matrix:
            row_s.add(min(row))
        for col in zip(*matrix):
            if max(col) in row_s:
                rs.append(max(col))
        return rs