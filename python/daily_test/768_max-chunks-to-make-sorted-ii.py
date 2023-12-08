from typing import List
from collections import deque
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        dq=deque([[arr[0],arr[0]]])
        for num in arr[1:]:
            if dq[-1][1]>num>dq[-1][0]:
                continue
            elif num>=dq[-1][1]:
                dq.append([num,num])
            elif num<dq[-1][0]:
                dq[-1][0]=num
        dq2=deque()
        dq2.append(dq.popleft())
        while dq:
            tmp_min,tmp_max=dq.popleft()
            while dq2 and tmp_min<dq2[-1][1]:
                pre_min,pre_max=dq2.pop()
                tmp_max=max(pre_max,tmp_max)
                tmp_min=min(pre_min,tmp_min)
            dq2.append([tmp_min,tmp_max])
        return len(dq2)


s=Solution()
print(s.maxChunksToSorted([0,3,0,3,2]))