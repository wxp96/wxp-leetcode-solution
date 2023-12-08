from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def sortColorSwap(i,j,n):
            while i<=j:
                if nums[i]!=n:
                    i+=1
                else:
                    nums[i],nums[j]=nums[j],nums[i]
                    if nums[i]!=n:
                        i+=1
                    j-=1
            return j
        i,j=0,len(nums)-1
        new_j=sortColorSwap(i,j,2)
        sortColorSwap(i,new_j,1)

s=Solution()
print(s.sortColors([1,0,1]))