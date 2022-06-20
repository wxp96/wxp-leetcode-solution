from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=set()
        res.add(())
        for num in nums:
            res_tmp=list(res)
            for i in res_tmp:
                i = list(i)
                i.append(num)
                res.add(tuple(sorted(i)))
        res=list(res)
        return list(map(list,res))
            