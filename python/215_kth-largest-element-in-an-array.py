from typing import List
from heapq import nlargest
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k,nums)[-1]

s=Solution()
print(s.findKthLargest([3,2,1,5,6,4],2))