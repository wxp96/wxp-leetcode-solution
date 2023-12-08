from typing import List
from functools import lru_cache
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        @lru_cache()
        def backtrack(arr):
            arr=list(arr)
            if len(arr)==1:
                return [arr]
            res=[]
            for i,num in enumerate(arr):
                nxt_track=backtrack(tuple(arr[0:i]+arr[i+1:]))
                for r_nums in nxt_track:
                    res.append([num]+r_nums)
            return res

        return backtrack(tuple(nums))

s=Solution()
print(s.permute([1,2,3]))
