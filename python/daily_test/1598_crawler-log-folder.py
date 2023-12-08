from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res=0
        for log in logs:
            log = log[:-1]
            if log=='..':
                if res >0:
                    res-=1
            elif log!='.':
                res+=1
        return res

s=Solution()
print(s.minOperations(["./","wz4/","../","mj2/","../","../","ik0/","il7/"]))