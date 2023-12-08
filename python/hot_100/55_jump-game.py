class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        fartherest=0
        i=0
        while i<=fartherest:
            fartherest=max(fartherest,nums[i]+i)
            if fartherest>=len(nums)-1:
                return True
            i+=1
        return False