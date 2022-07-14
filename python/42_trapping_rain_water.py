from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        lhest,rhest=height[l],height[r]
        res=0
        while l<r:
            while l<r and lhest<=rhest:
                res+=lhest-height[l]
                l+=1
                lhest=max(lhest,height[l])
            while l<r and lhest>rhest:
                res+=rhest-height[r]
                r-=1
                rhest=max(rhest,height[r])
        return res

s=Solution()
print(s.trap([4,2,0,3,2,5]))

