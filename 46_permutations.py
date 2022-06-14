from copy import deepcopy
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        length=len(nums)
        res=[]
        def backtrack(tmps,candidates):
            if len(tmps)==length:
                res.append(deepcopy(tmps))
                return
            for i,candidate in enumerate(candidates):
                tmps.append(candidate)
                backtrack(tmps,candidates[:i]+candidates[i+1:])
                tmps.pop()

        backtrack([],nums)
        return res