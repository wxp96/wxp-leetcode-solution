from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que=deque()
        for i in range(k):
            while que and que[-1]<nums[i]:
                que.pop()
            que.append(nums[i])
        ans=[que[0]]
        for i in range(k,len(nums)):
            while que and nums[i]>que[-1]:
                que.pop()
            que.append(nums[i])
            if nums[i-k]==que[0]:
                que.popleft()
            ans.append(que[0])
        return ans