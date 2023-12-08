from typing import List
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)//20
        arr.sort()
        arr1 = arr[n:-n]
        return sum(arr1)/len(arr1)


s=Solution()
print(s.trimMean([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]))