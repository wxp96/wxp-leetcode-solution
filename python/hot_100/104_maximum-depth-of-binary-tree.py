from python.lc_utils import TreeNode
from typing import Optional
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        left=right=0
        if not root:
            return 0
        if root.left:
            left=self.maxDepth(root.left)
        if root.right:
            right=self.maxDepth(root.right)
        return max(left,right)+1