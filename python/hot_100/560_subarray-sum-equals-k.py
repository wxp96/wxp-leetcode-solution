from typing import List
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dd=defaultdict(int)
        cur_sum=res=0
        dd[0]=1
        for num in nums:
            cur_sum+=num
            res+=dd[cur_sum-k]
            dd[cur_sum]+=1
            
        return res

    
s=Solution()
print(s.subarraySum([1,1,1],2))
                