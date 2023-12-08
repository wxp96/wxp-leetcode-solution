from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i,j):
            while i<=j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        nxt=-float('inf')
        i=len(nums)-1
        while i>=0 and nums[i]>=nxt:
            nxt=nums[i]
            i-=1
        if i==-1:
            swap(0,len(nums)-1)
            return
        j=len(nums)-1
        while j>=0 and nums[j]<=nums[i]:
            j-=1
        nums[i],nums[j]=nums[j],nums[i]
        swap(i+1,len(nums)-1)

s=Solution()
a=[6,2,1]
s.nextPermutation(a)
print(a)