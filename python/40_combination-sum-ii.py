from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(start,target):
            if target==0:
                res.append(temp[:])
                return
            if start==len(candidates) or target<candidates[start]:
                return
            for i in range(start,len(candidates)):
                if candidates[i]>target:
                    break
                if i!=start and candidates[i]==candidates[i-1]:
                    continue
                temp.append(candidates[i])
                backtrack(i+1,target-candidates[i])
                temp.pop()

        candidates=sorted(candidates)
        res=[]
        temp=[]
        backtrack(0,target)
        return res

s=Solution()
print(s.combinationSum2(candidates = [1], target = 2))