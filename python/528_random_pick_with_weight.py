from typing import List
from bisect import bisect_left
from random import randint
class Solution:

    def __init__(self, w: List[int]):
        self.pre_sum=[0]
        for weight in w:
            self.pre_sum.append(self.pre_sum[-1]+weight)

    def pickIndex(self) -> int:
        i=randint(1,self.pre_sum[-1])
        return bisect_left(self.pre_sum,i)-1



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()