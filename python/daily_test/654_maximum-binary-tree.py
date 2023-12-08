from typing import List,Optional
from python.lc_utils import TreeNode
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        max_v=0
        max_i=0
        for i,num in enumerate(nums):
            if num>max_v:
                max_v=num
                max_i=i
        root=TreeNode(max_v)
        root.left=self.constructMaximumBinaryTree(nums[:max_i])
        root.right=self.constructMaximumBinaryTree(nums[max_i+1:])
        return root