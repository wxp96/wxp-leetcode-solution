from typing import List
from sortedcollections import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res=[]
        tmp=SortedList()
        for num in nums[::-1]:
            i=tmp.bisect_left(num)
            res.append(i)
            tmp.add(num)
        return res[::-1]

s=Solution()
print(s.countSmaller([5,2,6,1,2,3,4]))
                    