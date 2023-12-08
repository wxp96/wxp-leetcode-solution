from typing import List
import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur=[[]]
        for num in nums:
            now=copy.deepcopy(cur)
            for s in now:
                s.append(num)
            cur.extend(now)
        return cur

s=Solution()
print(s.subsets([1,2,3]))