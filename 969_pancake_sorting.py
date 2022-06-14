from audioop import reverse
from typing import List
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        rs=[]
        n=len(arr)
        if n==1:
            return rs
        for i in range(n-1):
            if arr[i]==n:
                if i!=0:
                    rs.append(i+1)
                    arr=list(reversed(arr[:i+1]))+arr[i+1:]
                rs.append(n)
                arr.reverse()
                break
        rs+=self.pancakeSort(arr[:-1])
        return rs


s=Solution()
print(s.pancakeSort([3,2,4,1]))