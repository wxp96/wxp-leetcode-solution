from typing import Optional
from python.lc_utils import TreeNode
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def backtrack(root):
            if not root:
                return 0,0
            nonlocal res
            left=backtrack(root.left)
            right=backtrack(root.right)
            res=max(res,left+right+1)
            return max(left,right)+1
        
        res=0
        backtrack(root)
        return res