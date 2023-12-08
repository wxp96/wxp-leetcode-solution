from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return -1,-1
        l,r=0,len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]>=target:
                r=mid
        if l<len(nums) and nums[l]==target:
            left=l
        else:
            return -1,-1
        r=len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]<=target:
                l=mid+1
            elif nums[mid]>target:
                r=mid
        right=l-1
        return left,right

s=Solution()
print(s.searchRange([2,2],3))