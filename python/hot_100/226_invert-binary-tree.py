from typing import Optional
from lc_utils import TreeNode
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left=self.invertTree(root.left)
        right=self.invertTree(root.right)
        root.right=left
        root.left=right
        return root