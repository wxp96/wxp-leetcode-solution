from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left,right=0,len(nums1)
        m,n=len(nums1),len(nums2)
        if m>n:
            return self.findMedianSortedArrays(nums2,nums1)
        # if not m:
        #     midean1=nums2[(n-1)//2]
        #     midean2=nums2[n//2]
        while left<=right:
            i=(left+right)//2        
            j=(m+n+1)//2-i
            nums1im=nums1[i-1] if i!=0 else -float('inf')
            nums1i=nums1[i] if i!=m else float('inf')
            nums2jm=nums2[j-1] if j!=0 else -float('inf')
            nums2j=nums2[j] if j!=n else float('inf')

            if nums1im<=nums2j:
                midean1=max(nums1im,nums2jm)
                midean2=min(nums2j,nums1i)
                left=i+1
            else:
                right=i-1

        return midean1 if (m+n)%2 else (midean1+midean2)/2
        
s=Solution()
print(s.findMedianSortedArrays([1,3],[2,7]))
            