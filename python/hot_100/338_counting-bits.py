from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[0]*len(n)
        heighbit=0
        for i in range(n):
            if i&(i-1)==0:
                heighbit=i
            res[i]=res[i-heighbit]+1
        return res