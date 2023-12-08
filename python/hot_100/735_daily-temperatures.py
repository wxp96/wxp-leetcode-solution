from typing import List
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]
        dq=deque([temperatures[-1]])
        dq_i=deque([len(temperatures)-1])
        for i in range(len(temperatures)-2,-1,-1):
            while dq and temperatures[i]>=dq[-1]:
                dq.pop()
                dq_i.pop()
            if not dq_i:
                res.append(0)
            else:
                res.append(dq_i[-1]-i)
            dq.append(temperatures[i])
            dq_i.append(i)
        return res[::-1]
    
s=Solution()
print(s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))