from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        res_l=[0]*len(height)
        side_l,side_r=height[0],height[-1]
        while l<r:
            if height[l]<=height[r]:
                res_l[l]=side_l-height[l]
                l+=1
                side_l=max(side_l,height[l])
            else:
                res_l[r]=side_r-height[r]
                r-=1
                side_r=max(side_r,height[r])
        return sum(res_l)