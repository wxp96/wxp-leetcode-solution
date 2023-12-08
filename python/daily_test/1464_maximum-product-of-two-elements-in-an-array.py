from typing import List
import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums=[-num for num in nums]
        heapq.heapify(nums)
        i=heapq.heappop(nums)
        j=heapq.heappop(nums)
        return (i+1)*(j+1)
