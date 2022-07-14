from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(start,target):
            if target==0:
                res.append(temp[:])
                return
            if target<candidates[0]:
                return
            for i in range(start,len(candidates)):
                if candidates[i]>target:
                    break
                temp.append(candidates[i])
                backtrack(i,target-candidates[i])
                temp.pop()

        candidates=sorted(candidates)
        res=[]
        temp=[]
        backtrack(0,target)
        return res

s=Solution()
print(s.combinationSum([2,3,6,7],7))