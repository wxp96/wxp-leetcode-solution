from typing import List
import bisect,heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i=bisect.bisect_left(arr,x)
        l=max(0,i-k)
        r=min(len(arr),i+k)
        while r-l>k:
            l_diff=abs(arr[l]-x)
            r_diff=abs(arr[r-1]-x)
            if l_diff>r_diff:
                l+=1
            else:
                r-=1
        return arr[l:r]

s=Solution()
print(s.findClosestElements([1,2,3,4,5],4,3))