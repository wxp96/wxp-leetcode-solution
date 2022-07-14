from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs=sorted(pairs,key=lambda x:x[1])
        res=[pairs[0]]
        right=[pairs[0][1]]
        for pair in pairs[1:]:
            if pair[0]>res[-1][1]:
                res.append(pair)
        return len(res)

s=Solution()
s.findLongestChain([[1,2],[7,8],[4,5]])