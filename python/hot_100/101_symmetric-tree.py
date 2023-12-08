from typing import Optional
from python.lc_utils import TreeNode
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def inner(left,right):
            if not left:
                return not right
            if not right:
                return not left
            if left.val!=right.val:
                return False
            first=inner(left.left,right.right)
            second=inner(left.right,right.left)
            return first and second

        return inner(root.left,root.right)