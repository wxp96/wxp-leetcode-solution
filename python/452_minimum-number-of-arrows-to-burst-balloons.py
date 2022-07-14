from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points=sorted(points,key=lambda x:x[1])
        pre_i,pre_j=points[0]
        res=1
        for i,j in points[1:]:
            if i<=pre_j:
                pre_i=i
            else:
                res+=1
                pre_i,pre_j=i,j
        return res
