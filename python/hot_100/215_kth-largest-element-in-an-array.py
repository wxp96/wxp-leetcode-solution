from typing import List
from random import randint
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quicksort(nums,k):
            if len(nums)==1 and k==1:
                return nums[0]
            sentry=randint(0,len(nums)-1)
            nums[sentry],nums[-1]=nums[-1],nums[sentry]
            i=0
            for j in range(len(nums)-1):
                if nums[j]>nums[-1]:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
            nums[-1],nums[i]=nums[i],nums[-1]
            if i==k-1:
                return nums[i]
            elif i>=k:
                return quicksort(nums[:i],k)
            else:
                return quicksort(nums[i+1:],k-i-1)
            
        return quicksort(nums,k)
                    
s=Solution()
print(s.findKthLargest([3,2,1,5,6,4],2))

            
s=Solution()
print(s.findKthLargest([-1,2,0], k = 1))