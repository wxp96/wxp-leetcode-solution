from typing import Optional
from python.lc_utils import TreeNode
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def backtrack(root):
            nonlocal memo
            if not root:
                return
            backtrack(root.left)
            memo+=root.val
            root.val=memo
            backtrack(root.right)

        memo=0
        backtrack(root)
        return root

        