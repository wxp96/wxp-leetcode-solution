from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(remain,i):
            if remain==0:
                result.append(item[:])
                return
            if i>=len(candidates):
                return
            j=i-1
            for can in candidates[i:]:
                if can>remain:
                    break
                j+=1
                item.append(can)
                dfs(remain-can,j)
                item.pop()
        result=[]
        item=[]
        candidates.sort()
        dfs(target,0)
        return result

s=Solution()
print(s.combinationSum(candidates = [2,3,6,7], target = 7))