from typing import List
from copy import deepcopy
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtrack(idx,start,remain):
            if idx==k:
                if remain==0:
                    res.append(deepcopy(temp))
                else:
                    return
            
            for i in range(start,10):
                if i>remain:
                    break
                temp[idx]=i
                backtrack(idx+1,i+1,remain-i)

        res=[]
        temp=[0]*k
        backtrack(0,1,n)
        return res

s=Solution()
print(s.combinationSum3(2,18))