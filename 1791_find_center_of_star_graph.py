from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x,y = edges[1]
        if x in edges[0]:
            return x
        else:
            return y