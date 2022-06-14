from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        pre=None
        for i in range(len(bits)-1):
            if bits[i]==1:
                if pre==1:
                    pre=None
                else:
                    pre=1
            else:
                pre=None
        if pre==None and bits[-1]==0:
            return True
        else:
            return False

s=Solution()
print(s.isOneBitCharacter([1,0,0]))