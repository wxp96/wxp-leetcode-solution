from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.sums=[0]
        for i in range(len(nums)):
            self.sums.append(self.sums[-1]+nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right+1]-self.sums[left]